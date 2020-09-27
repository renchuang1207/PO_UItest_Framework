class ExcelVariable:
    cassid=0
    header=1
    url=2
    data=3
    expect=4
    result=5


def getcassId():
    return ExcelVariable.cassid

def getHeader():
    return ExcelVariable.header

def getUrl():
    return ExcelVariable.url

def getData():
    return ExcelVariable.data

def getExpect():
    return ExcelVariable.expect

def getResult():
    return ExcelVariable.result