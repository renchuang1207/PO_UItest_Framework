import logging
import os
import time

from utils.YamlHandler import yaml_data


class LoggerHandler(logging.Logger):
    # 继承Logger类
    def __init__(self,
                 name='root',
                 level='DEBUG',
                 file=None,
                 format=None
                 ):
        # 设置收集器
        super().__init__(name)
        # 设置收集器级别
        self.setLevel(level)
        # 设置日志格式
        fmt = logging.Formatter(format)
        # 如果存在文件，就设置文件处理器，日志输出到文件
        if file:
            file_handler = logging.FileHandler(file,encoding='utf-8')
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        # 设置StreamHandler,输出日志到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)
# 从yaml配置文件中读取logging相关配置
now_time = time.strftime('%Y-%m-%d')
log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'logs/log_%s.txt'%now_time)
logger = LoggerHandler(name=yaml_data['logger']['name'],
                       level=yaml_data['logger']['level'],
                       file=log_dir,
                       format=yaml_data['logger']['format'])

if __name__ == '__main__':
    logger.info('这是一条测试的日志')