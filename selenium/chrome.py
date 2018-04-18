import time
from selenium import webdriver

if __name__ == "__main__":
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.baidu.com');
    # time.sleep(3) # Let the user actually see something!
    # search_box = driver.find_element_by_name('wd')
    # search_box.send_keys('selenium')
    # search_box.submit()
    # time.sleep(3) # Let the user actually see something!
    # driver.quit()

# from selenium import webdriver
#
#
# if __name__ == "__main__":
#     driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
#     driver.get("http://www.baidu.com")
#     driver.find_element_by_id('kw').send_keys('selenium')
#     driver.find_element_by_id('su').click()
#     driver.quit()
