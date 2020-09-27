from common.base_page import BasePage
from common.browser import Browser
from common.element_data_uitls import ElementDataUtils


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        elements = ElementDataUtils('main', 'main_page').get_element_info()
        self.myzone_link = elements['myzone_link']
        self.user_menu = elements['user_menu']
        self.quit_button = elements['quit_button']
        
    def goto_myzone(self):#进入我的地盘菜单
        self.click(self.myzone_link)
        
    def get_username_value(self):
        value = self.get_text(self.user_menu)
        return value
    
    def click_username(self):
        self.click(self.user_menu)
    
    def click_quit_button(self):
        self.click(self.quit_button)
    
