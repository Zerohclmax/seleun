from selenium import webdriver

url = "http://www.pythontip.com/user/login"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
browser.find_element_by_xpath('//*[@id="editor_name"]').send_keys('PythonXC')
browser.find_element_by_xpath('//*[@id="editor_pwd"]').send_keys('pythonxiaocai')
browser.find_element_by_xpath('//*[@id="apLogin"]/fieldset/div[3]/input').click()


