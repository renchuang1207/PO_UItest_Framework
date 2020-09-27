import json

import xlrd

from common.public import filepath
from utils.excel_data import *


class OperationExcel:
    def __init__(self,fileDir,filename):
        self.fileDir = fileDir
        self.filename = filename
        
    def getExcel(self):
        excel=xlrd.open_workbook(filepath(fileDir=self.fileDir,filename=self.filename))
        sheet=excel.sheet_by_index(0)
        return sheet
    def get_rows(self):
        """获取Excel行数"""
        return self.getExcel().nrows
    def get_values(self,row,rol):
        """获取单元格的值"""
        return self.getExcel().cell_value(row,rol)
    def get_cassid(self,row):
        return self.get_values(row,getcassId())
    def get_url(self,row):
        return self.get_values(row,getUrl())
    def get_data(self,row):
        return self.get_values(row,getData())
    def get_header(self,token,row):
        # return self.get_values(row,getHeader())
        token1 = 'Bearer' + ' ' + token
        hearder = json.loads(self.get_values(row,getHeader()))
        hearder['Authorization'] = token1
        return hearder

