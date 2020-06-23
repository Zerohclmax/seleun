from selenium import webdriver
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_argument('--headless')
browser = webdriver.Chrome(options=option)

url = 'https://www.baidu.com'
browser.get(url)
browser.save_screenshot('baidu.png')