import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common.config_utils import local_config
from utils.LoggerHandler import logger

current_path = os.path.abspath(os.path.dirname(__file__))
driver_path = os.path.join(current_path,'..',local_config.driver_path)

class Browser(object):
    def __init__(self,path = driver_path,driver_name = local_config.driver_name):
        self.__driver_path = path
        self.__driver_name = driver_name

    def get_driver(self):
        if self.__driver_name.lower() == 'chrome':#lower()把大写变为小写的方法
            return self.__get_chrome_driver()
        elif self.__driver_name.lower() == 'firefox':
            return self.__get_firefox_driver()

    def __get_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')#谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')#设置默认编码为utf-8
        prefs = {}
        prefs['credentials_enable_service'] = False
        prefs['profile.password_manager_enabled'] = False
        chrome_options.add_experimental_option('prefs', prefs)  # 关闭登录后密码提示弹窗
        chrome_options.add_experimental_option('useAutomationExtension',False)#取消chrome受自动化控制提示
        chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])#取消chrome受自动化控制提示
        chrome_options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
        driver_path = os.path.join(self.__driver_path, 'chromedriver')
        driver = webdriver.Chrome(options=chrome_options,executable_path=driver_path)
        logger.info('初始化并启动浏谷歌浏览器')
        return driver

    def __get_firefox_driver(self):
        driver_path = os.path.join(self.__driver_path, 'geckdriver.exe')
        driver = webdriver.Chrome(executable_path=driver_path)
        return driver


if __name__ == '__main__':
    f = Browser()
    f.get_driver()
