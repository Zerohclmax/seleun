from selenium import webdriver
from selenium.webdriver import ChromeOptions


option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(options=option)

# 关闭自动化扩展信息
option.add_experimental_option('useAutomationExtension',False)

browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{'source':'Object.defineProperty(navigator,"webdriver",{get:()=>undefined})'})




url = 'https://www.zhipin.com/'
browser.get(url)

# 输入职位
browser.find_element_by_xpath('//*[@id="wrap"]/div[4]/div/div/div[1]/form/div[2]/p/input').send_keys('Python')
# 点击搜索
browser.find_element_by_xpath('//*[@id="wrap"]/div[4]/div/div/div[1]/form/button').click()