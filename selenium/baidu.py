import time
from selenium import webdriver

if __name__ == "__main__":
    driver = webdriver.Chrome()
    #打开百度
    driver.get('https://www.baidu.com')
    #页面加载3分钟
    time.sleep(3)
    driver.find_element_by_link_text('登录').click()
    time.sleep(3)
    driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
    time.sleep(3)
    #找到登录名输入框
    Username=driver.find_element_by_id('TANGRAM__PSP_10__userName')
    #输入登录名
    Username.send_keys('000000')
    #找到输入密码框
    Password=driver.find_element_by_id('TANGRAM__PSP_10__password')
    #输入密码
    Password.send_keys('0000000.')
    time.sleep(10)
    #找到登录密码
    Login_form=driver.find_element_by_id('TANGRAM__PSP_10__submit')
    #点击登录按钮
    Login_form.click()
    #等待3秒
    #time.sleep(30)
    #driver.quit()