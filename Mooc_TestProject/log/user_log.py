import logging
import os
import datetime

class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 控制台输出日志
        # console = logging.StreamHandler()
        # logger.addHandler(console)
        # 文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        log_name = log_dir+ "\\"+ log_file
        print(log_name)

        # 文件输出日志
        self.file_handle = logging.FileHandler(log_name, "a", encoding="utf-8")
        self.logger.setLevel(logging.INFO)
        # formatter指定日志记录输出具体格式
        formatter = logging.Formatter("%(asctime)s %(filename)s--> %(funcName)s %(lineno)d: %(levelno)s -->%(message)s ")
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)


        # self.logger.removeHandler(file_handle)
        # file_handle.close()
        # console.close()
        # logger.removeHandler(console)
    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == "__main__":
    user = UserLog()
    log = user.get_log()
    log.debug("test")
    user.close_handle()