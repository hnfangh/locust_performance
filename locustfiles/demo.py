
from locust import HttpUser,task,between,tag
from common.baselocust import BaseLocust
from common.log import Log

class MyUser(HttpUser,BaseLocust):

    wait_time = between(1,2)
    host = "https://xxx.xxx.cn"
    _log = Log()

    def on_start(self):
        self.on_test_start()

    def on_stop(self):
         self.on_test_stop()

    @tag('登录')
    @task
    def login(self):
        with  self.client.post("/api/xxx/xxx/login/",json={"password":"xxx==","phoneNumber":"xxx","uuid":"xxx","loginType":1,"isPlugin":True},headers={"content-type": "application/json;charset=UTF-8"},catch_response=True) as response:
            if response.status_code == 200 and response.json()["code"] == 0:
                response.success()
                self._log.info("请求成功<===================={}".format(response.json()["msg"]))
            else:
                response.failure()
                self._log.error("请求失败<===================={}".format(response.json()["msg"]))

def get_asin():
    return ["B09DX19xxx", "B09M816xxx", "B09M7ZYxxx"]

