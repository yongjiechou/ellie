from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup

url='https://es2.nnkieh.tn.edu.tw/haksing/modules/yh_aftersch/index.php'
driver = webdriver.Chrome()
driver.get(url)
s1 = Select(driver.find_element_by_id('sltDept'))  # 例項化Select
s1.select_by_index(1)
driver.find_element_by_xpath('//*[@id="StudPid"]').send_keys('3799')
driver.find_element_by_xpath('//*[@id="StudBirth"]').send_keys('0621')
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
res=requests.get(url).text
html = BeautifulSoup(res,'lxml')
content = html.find_all("td")
##driver.close()