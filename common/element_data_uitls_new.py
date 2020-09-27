import os
from common.config_utils import local_config
from common.excel_utils import ExcelUtils

current_path = os.path.dirname(os.path.dirname(__file__))
excel_path = os.path.join(current_path,'element_info_datas/element_infos.xlsx')

class ElementDataUtilsNew(ExcelUtils):
	def __init__(self,excel_path,page_name,sheet_name=None):
		super().__init__(excel_path,sheet_name)
		self.page_name = page_name

	def get_element_info(self):
		element_infos = {}
		for i in range(1,self.get_row_count):
			if self.sheet_data.cell_value(i, 2) == self.page_name:
				element_info = {}
				element_info['element_name'] = self.sheet_data.cell_value(i, 1)
				element_info['locator_type'] = self.sheet_data.cell_value(i, 3)
				element_info['locator_value'] = self.sheet_data.cell_value(i, 4)
				timeout_value = self.sheet_data.cell_value(i, 5)
				element_info['timeout'] = timeout_value if isinstance(timeout_value, float) else local_config.timeout
				element_infos[self.sheet_data.cell_value(i, 0)] = element_info
		return element_infos
	
	def get_element_infos(self):
		element_infos = {}
		for i in range(1, self.get_row_count):
			if self.get_sheet_data_by_list()[i][2] == self.page_name:
				element_info = {}
				element_info['element_name'] = self.get_sheet_data_by_list()[i][1]
				element_info['locator_type'] = self.get_sheet_data_by_list()[i][3]
				element_info['locator_value'] = self.get_sheet_data_by_list()[i][4]
				timeout_value = self.get_sheet_data_by_list()[i][5]
				element_info['timeout'] = timeout_value if isinstance(timeout_value, float) else local_config.timeout
				element_infos[self.get_sheet_data_by_list()[i][0]] = element_info
		return element_infos
		
	


if __name__ == '__main__':
    test = ElementDataUtilsNew(excel_path,'login_page')
    elements = test.get_element_info()
    print(elements)
    for value in elements.values():
	    print(value)
