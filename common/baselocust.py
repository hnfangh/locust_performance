
from common.log import Log
from locust import events

"""
More than 1% of the requests failed
The average response time is longer than 200 ms
The 95th percentile for response time is larger than 800 ms
"""

class BaseLocust:

    _log = Log()

    # todo 结果监听
    """
    满足以上任何条件，则将退出代码设置为非零：
    超过0.01 的请求失败
    平均响应时间大于2000ms
    响应时间的第95个百分位数大于5000毫秒
    """
    @events.quitting.add_listener
    def _env(self,environment):
        if environment.stats.total.fail_ratio > 0.01:
            self._log.error("Test failed due to failure ratio > 1%")
            environment.process_exit_code = 1
        elif environment.stats.total.avg_response_time > 800:
            self._log.error("Test failed due to average response time ratio > 200 ms")
            environment.process_exit_code = 1
        elif environment.stats.total.get_response_time_percentile(0.95)>800:
            self._log.error("Test failed due to 95th percentile response time > 800 ms")
            environment.process_exit_code = 1
        else:
            environment.process_exit_code = 0

    # todo 开始
    @events.test_start.add_listener
    def on_test_start(self):
        self._log.info("【压测开始】locusts runner started <=================")

    # todo 结束
    @events.test_stop.add_listener()
    def on_test_stop(self):
        self._log.info("【压测结束】locust runner stopped <=================")
        self._env.runner.quit()


