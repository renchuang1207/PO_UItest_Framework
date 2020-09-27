import unittest
from common.base_page import BasePage
from common.browser import Browser
from actions.login_action import LoginAction
from common.config_utils import local_config
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class LoinTest(SeleniumBaseCase):
	test_calss_data = TestDataUtils('login_suite', 'LoinTest').convert_exceldata_to_testdata()
	def setUp(self) -> None:
		super().setUp()

	@unittest.skipIf(test_calss_data['test_login_success']['isnot'],'')
	def test_login_success(self):
		test_function_data = self.test_calss_data['test_login_success']
		self._testMethodDoc = test_function_data['test_name']
		login_action = LoginAction(self.base_page.driver)
		mainpage = login_action.login_success(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
		actual_result = mainpage.get_username_value()
		self.assertEqual(actual_result,test_function_data['excepted_result'],'test_login_success用例执行失败')
	
	def test_login_fail(self):
		test_function_data = self.test_calss_data['test_login_fail']
		self._testMethodDoc = test_function_data['test_name']
		login_action = LoginAction(self.base_page.driver)
		actual_result = login_action.login_fail(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
		self.assertEqual(actual_result, test_function_data['excepted_result'])
		
		
if __name__ == '__main__':
    unittest.main()
	
		
	

