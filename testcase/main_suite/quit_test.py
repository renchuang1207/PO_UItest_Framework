import unittest
from actions.quit_action import QuitAction
from actions.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase


class LoinTest(SeleniumBaseCase):
	def test_quit(self):
		login_action = LoginAction(self.base_page.driver)
		main_page = login_action.default_login()
		quit_action = QuitAction(main_page.driver)
		login_page = quit_action.quit()
		acctual_result = login_page.get_title()
		self.assertEqual(acctual_result.__contains__('用户登录'),True,'test_quit用例不通过')
		
if __name__ == '__main__':
    unittest.main()