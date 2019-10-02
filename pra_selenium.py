import time
import datetime
from selenium import webdriver         #匯入 webdriver 模組
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.common.exceptions import NoSuchElementException  
        
if __name__ == '__main__':
    # browser=webdriver.Chrome()#開啟模擬瀏覽器
    # urls=["http://www.google.com.tw",     #URL 串列
    # "http://tw.yahoo.com", 
    # "https://twitter.com"]
    # for url in urls: #依序開啟網頁 (最後停在 Twitter)
    #     browser.get(url)
    # browser.back()                                        #回前一頁 (YAHOO)
    
    driver = webdriver.Chrome()
    driver.get("http://140.113.209.24/0656000")
    
    assert "Title" in driver.title
    elem = driver.find_element_by_xpath('//*[@id="id"]')
    id = (elem.text)
    print(id)
    elem = driver.find_element_by_xpath('//*[@id="time"]')
    time = (elem.text)
    print(time)
    elem = driver.find_element_by_xpath('//*[@id="secret"]')
    hash = (elem.text)
    print(hash)
    # driver.get("https://www.google.com")
    # #找到輸入框
    # element = driver.find_element_by_name("q");
    # #輸入內容
    # element.send_keys("hello world");
    # #提交表單
    # element.submit();

    # caps = DesiredCapabilities.INTERNETEXPLORER
    # caps['requireWindowFocus'] = True
    # driver_ie="C:\\Users\\yaqi.zhang\\Downloads\\\IEDriverServer_Win32_2.42.0\\IEDriverServer.exe";
    # driver=webdriver.Ie(driver_ie,capabilities=caps)
    pass