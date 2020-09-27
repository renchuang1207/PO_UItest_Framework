# -*-coding:UTF-8-*-
import logging
import os
import time


class Logger(object):
    """
    终端打印不同颜色的日志，在pycharm中如果强行规定了日志的颜色， 这个方法不会起作用， 但是
    对于终端，这个方法是可以打印不同颜色的日志的。
    """
    logger = logging.getLogger("root")
    logger.setLevel(logging.DEBUG)

  
    tool_log_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "logs")
    if not os.path.exists(tool_log_path):
        os.makedirs(tool_log_path)
    tool_log_file = os.path.normpath(os.path.join(tool_log_path, "tool_log" + time.strftime("%Y%m%d", time.localtime())+ ".log"))
    # 创建一个handler,用于写入日志文件
    tool_log = logging.FileHandler(
        tool_log_file,
        encoding='utf-8')
    tool_log.set_name('tool_log')
    tool_log.setLevel(logging.INFO)

    # 控制台输出
    console = logging.StreamHandler()
    console.set_name('console')
    tool_log.setLevel(logging.DEBUG)


    # 定义handler的输出格式
    formatter = logging.Formatter('[%(filename)s] - [%(asctime)s] - [%(levelname)s] - %(message)s')

    # handler添加format
    console.setFormatter(formatter)
    tool_log.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(console)
    logger.addHandler(tool_log)

   
    @classmethod
    def debug(cls, message, *args, **kwargs):
        """
        输出调试信息

        :param message: 调试信息
        :return:
        """
        cls.fontColor('\033[0;32m%s\033[0m')
        cls.logger.debug(message, *args, **kwargs)

    @classmethod
    def info(cls, message, *args, **kwargs):
        """
        输出程序运行详细信息

        :param message: 详细信息
        :return:
        """
        cls.fontColor('\033[0;34m%s\033[0m')
        cls.logger.info(message, *args, **kwargs)

    @classmethod
    def warning(cls, message, *args, **kwargs):
        """
        输出程序运行警告信息

        :param message: 警告信息
        :return:
        """
        cls.fontColor('\033[0;37m%s\033[0m')
        cls.logger.warning(message, *args, **kwargs)

    @classmethod
    def error(cls, message, *args, **kwargs):
        """
        输出程序运行错误信息

        :param message: 错误信息
        :return:
        """
        cls.fontColor('\033[0;31m%s\033[0m')
        cls.logger.error(message, *args, **kwargs)

    @classmethod
    def critical(cls, message, *args, **kwargs):
        """
        输出程序运行严重错误信息

        :param message: 错误信息
        :return:
        """
        cls.fontColor('\033[0;35m%s\033[0m')
        cls.logger.critical(message, *args, **kwargs)

    @classmethod
    def fontColor(cls, color):
        """
        更改控制台输出的日志颜色

        :param color: 颜色种类
        :return:
        """
        formatter = logging.Formatter(color % '[%(asctime)s] - [%(levelname)s] - %(message)s')
        cls.console.setFormatter(formatter)
        
logger = Logger()



if __name__ == "__main__":
    logger.info('这是一条info日志')
    logger.error('这是一条错误级别的日志')
    logger.debug('这是一条debug级别的日志')
 

