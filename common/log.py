import sys
from loguru import logger as log

class Log:


    # 设置输出的日志级别
    # format = "{time:YYYY-MM-DD hh:mm:ss} - {level} - {filename}:{line} - {message}"
    # log.add(sys.stdout,level="DEBUG") 设置工作台打印日志级别

    def info(self,msg:str):
        return log.info(msg)

    def debug(self,msg:str):
        return log.debug(msg)

    def warning(self,msg:str):
        return log.warning(msg)

    def error(self,msg:str):
        return log.error(msg)

if __name__ == "__main__":
    _log = Log()
    _log.error("this is log information<<<<<<<<<<<<<<")

