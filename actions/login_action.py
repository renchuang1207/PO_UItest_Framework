from common.config_utils import local_config
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage


class LoginAction(object):
	def __init__(self,driver):
		self.login_page = LoginPage(driver)
		
	def login_action(self,username,password):
		self.login_page.clear_input_username()
		self.login_page.input_username(username)
		self.login_page.clear_input_password()
		self.login_page.input_password(password)
		self.login_page.click_login()
		
	def login_success(self,username,password):
		self.login_action(username,password)
		return MainPage(self.login_page.driver)
	
	def default_login(self):
		return self.login_success(local_config.user_name,local_config.password)
	
	def login_fail(self,username,password):
		self.login_action(username,password)
		return  self.login_page.get_login_fail_alert_content()


