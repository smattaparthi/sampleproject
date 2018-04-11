
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("https://docs.python.org")
abc = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div[1]/ul[1]/li")
print abc
print len(abc)
print type(abc)
# links = [1,2,3]
for everylink in range(1, len(abc)+1):
    icon = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[1]/li[%s]/a'%everylink)
    sleep(5)
    icon.click()
driver.close()

