import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from utils.LoggerHandler import logger
from selenium.webdriver.common.by import By
from common.config_utils import local_config
from selenium.webdriver.common.action_chains import ActionChains


current_dir = os.path.dirname(os.path.dirname(__file__))

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
        self.chains = ActionChains(self.driver)


    #浏览器的操作封装-->二次封装
    def open_url(self,url):
        """
        打开网址
        :param url: 浏览器url
        :return:
        """
        try:
            self.driver.get(url)
            logger.info('打开URL地址{0}'.format(url))
        except Exception as e:
            logger.error('不能打开指定的测试网址，原因是：{0}'.format(e.__str__()))
    
    
    
    def set_browser_max(self):
        """
        浏览器最大化
        :return:
        """
        self.driver.maximize_window()
        logger.info('设置浏览器最大化')
        
    
    def set_browser_min(self):
        """
        浏览器最小化
        :return:
        """
        self.driver.minimize_window()
        logger.info('设置浏览器最小化')
        
    
    def implicitly_wait(self,seconds=local_config.timeout):
        """
        隐士等待的封装
        :param seconds: 等待时间
        :return:
        """
        self.driver.implicitly_wait(seconds)
    
    
    def refresh_browser(self):
        """
        浏览器刷新操作
        :return:
        """
        self.driver.refresh()
        logger.info('浏览器刷新操作')
    
    
    def get_title(self):
        """
        获取网页标题
        :return:
        """
        value = self.driver.title
        logger.info('获取网页标题，标题是:{0}'.format(value))
        return value
    
    
    def quit_browser(self):
        """
        退出浏览器
        :return:
        """
        self.driver.quit()
        logger.info('退出浏览器')
    
    
    
    def find_element(self,element_info):
        """
        显示等待识别元素
        :param element_info:元素的字典{'element':'用户名输入框','locator_type':'xpath','locator_value':'//input[@id="account"]','timeput':5}
        :return:元素对象
        """
        try:
            locator_type_name = element_info['locator_type']
            locator_value_info = element_info['locator_value']
            locator_timeout = element_info['timeout']
            if locator_type_name == 'id':
                locator_type = By.ID
            elif locator_type_name == 'class':
                locator_type = By.CLASS_NAME
            elif locator_type_name == 'xpath':
                locator_type = By.XPATH
            elif locator_type_name =='name':
                locator_type = By.NAME
            element = WebDriverWait(self.driver , locator_timeout)\
                .until(lambda x:x.find_element(locator_type,locator_value_info))
            logger.info('[{0}]元素识别成功'.format(element_info['element_name']))
        except Exception as e:
            logger.error('[{0}]元素不能识别，原因是{1}'.format(element_info['element_name'],e.__str__()))
            self.screenshot_as_file()
        # finally:
        #     if element is None:
        #         element = ''
        return element
    
    
    def click(self,element_info):
        """
        点击操作
        :param element_info: 元素的字典
        :return:
        """
        element = self.find_element(element_info)
        try:
            element.click()
            logger.info('[{0}]元素进行点击操作成功'.format(element_info['element_name']))
        except Exception as e:
            logger.error('[{0}]元素点击操作失败，原因是{1}'.format(element_info['element_name'],e.__str__()))
        
    
    def send_keys(self,element_info,content):
        """
        输入操作
        :param element_info:
        :param content: 输入的值
        :return:
        """
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[{0}]元素输入信息操作成功,输入的信息为:{1}'.format(element_info['element_name'],content))
    
    
    #获取元素文本
    def get_text(self,element_info):
        element = self.find_element(element_info)
        return element.text
    
    
    
    #清楚输入框操作
    def clear(self,element_info):
        element = self.find_element(element_info)
        element.clear()
        logger.info('[{0}]输入框信息清除操作成功'.format(element_info['element_name']))
        
      
        
    #鼠标键盘封装（建议代码思路：判断操作系统类型）
    def move_to_element_by_mouse(self,element_info):
        """
        鼠标移动到某元素上
        :param element_info: 元素的字典
        :return:
        """
        element = self.find_element(element_info)
        self.chains.move_to_element(element).perform()
        
    
    def long_press_element(self,element_info,senconds):
        """
        鼠标长按某元素
        :param element_info: 元素的字典
        :param senconds: 长按秒数
        :return:
        """
        element = self.find_element(element_info)
        self.chains.click_and_hold(element).pause(senconds).release(element)
    
    
    #selenium执行js
    def execute_script(self,js_str,element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str,None)
    
    
    #移除元素属性
    def remove_element_attribute(self,element_info,attribute_name):
        element = self.find_element(element_info)
        self.execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)
    
        
    #修改元素属性
    def uodate_element_attribute(self,element_info,attribute_name,attribute_value):
        element = self.find_element(element_info)
        self.execute_script('arguments[0].removeAttribute("%s","%s");'%(attribute_name,attribute_value),element)
        
    
        
    #frame == 》id/name frame元素对象
    #思路一，不要id和name
    def swtich_to_frame(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
    
    
    #思路二
    def stitch_to_frame_by_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)
    
    
    def swtich_to_frame_by_element(self, element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
    
        
    #思路三
    def swtich_to_frame_dict(self,**element_dict): #swtich_to_frame(id=frameid)
        self.wait(3)
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])
        elif 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            element = self.find_element(element_dict['element'])
            self.driver.switch_to.frame(element)
    
    
    def switch_to_alert(self,action = 'accept',time_out = local_config.timeout):
        """
        alert弹窗的封装
        :param action: alert弹窗操作方式1、accept  2、dismiss
        :param time_out: 超时时间
        :return:
        """
        WebDriverWait(self.driver,time_out).until(EC.alert_is_present())
        alter = self.driver.switch_to.alert
        alter_text=alter.text
        if action =='accept':
            alter.accept()
        else:
            alter.dismiss()
        return alter_text
    
    
    def get_window_handle(self):
        """
        获取当前窗口的句柄
        :return: 返回当前窗口的句柄
        """
        return self.driver.current_window_handle
    
    
    def switch_to_window_by_handle(self,window_handle):
        """
        切换窗口
        :param window_handle: 切换的句柄
        :return:
        """
        self.driver.switch_to.window(window_handle)
    
    
    def swtch_to_window_by_title(self,title):
        """
        根据窗口title切换窗口
        :param title: 窗口title
        :return:
        """
        window_handles = self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver,local_config.timeout).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                break
        
    
    def swtch_to_window_by_url(self,url):
        """
        根据窗口url切换窗口
        :param url: 窗口的url
        :return:
        """
        window_handles = self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver,local_config.timeout).until(EC.url_contains(url)):
                self.driver.switch_to.window(window_handle)
                break
    
    
    def screenshot_as_file(self,*screenshot_path):
        """
        截图封装
        :param screenshot_path: 路径元组
        :return:
        """
        if len(screenshot_path) == 0:
            screenshot_filepath = local_config.screenshot_path
        else:
            screenshot_filepath = screenshot_path[0]
        now_time = time.strftime('%Y-%m-%d_%H:%M:%S')
        screenshot_filepath = os.path.join(current_dir,screenshot_filepath,'UITest_%s.png' % now_time)
        self.driver.get_screenshot_as_file(screenshot_filepath)
            
    
    def wait(self,seconds=local_config.timeout):
        """
        固定时间等待的封装
        :param seconds: 等待时间
        :return:
        """
        time.sleep(seconds)

