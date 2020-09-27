from actions.login_action import LoginAction
from common.browser import Browser

driver = Browser().get_driver()
driver.get('https://www.baidu.com')
s = driver.find_elements_by_xpath('//*[@class="mnav c-font-normal c-color-t"]')
driver.find_elements()
print(s)