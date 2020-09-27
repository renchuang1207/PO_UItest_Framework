import os
from common.excel_utils import ExcelUtils
from common.config_utils import local_config


current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path,'..',local_config.testdata_path)


class TestDataUtils():
	def __init__(self,test_suite_name,test_class_name):
		self.test_class_name = test_class_name
		self.excel_data = ExcelUtils(excel_path,'login_suite').get_sheet_data_by_list()
		self.excel_rows = len(self.excel_data)
		
	def convert_exceldata_to_testdata(self):
		test_data_infos = {}
		for i in range(1,self.excel_rows):
			test_data_info = {}
			if self.excel_data[i][2] == self.test_class_name:
				test_data_info['test_name'] = self.excel_data[i][1]
				test_data_info['isnot'] = False if self.excel_data[i][3].__eq__('是') else True
				test_data_info['excepted_result'] = self.excel_data[i][4]
				test_parameter = {}
				for j in range(5,len(self.excel_data[i])):
					if self.excel_data[i][j].__contains__('=') and len(self.excel_data[i][j])>2:
						parameter = self.excel_data[i][j].split('=')
						test_parameter[parameter[0]] = parameter[1]
				test_data_info['test_parameter'] = test_parameter
			test_data_infos[self.excel_data[i][0]] = test_data_info
		return test_data_infos
		
		
if __name__ == '__main__':
    test = TestDataUtils('login_suite','LoinTest')
    elements = test.convert_exceldata_to_testdata()
    for key,value in elements.items():
	    print(key,':',value)