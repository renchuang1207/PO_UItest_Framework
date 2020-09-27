from common.base_page import BasePage
from common.browser import Browser
from common.element_data_uitls import ElementDataUtils


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        elements = ElementDataUtils('login','login_page').get_element_info()
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']
    #方法==》控件的操作
    def input_username(self,username):
        self.send_keys(self.username_inputbox, username)
 
    def input_password(self,password):
        self.send_keys(self.password_inputbox,password)
    
    def clear_input_username(self):
        self.clear(self.username_inputbox)
    
    def clear_input_password(self):
        self.clear(self.password_inputbox)
 
    def click_login(self):
        self.click(self.login_button)
    
    def get_login_fail_alert_content(self):
        return self.switch_to_alert()
        

if __name__ == '__main__':
    driver = Browser().get_driver()
    login_page = LoginPage(driver)
    login_page.open_url('http://localhost/zentaopms/www/user-login.html')
    login_page.set_browser_max()
    login_page.input_username('admin')
    login_page.input_password('rc15892367305')
    login_page.click_login()
    login_page.screenshot_as_file()