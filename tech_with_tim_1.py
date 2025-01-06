

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def page(user_name_data,password_data):
    url="https://www.saucedemo.com/"
    driver=webdriver.Chrome()
    main_page=driver.get(url=url)
    #add password and login
    username=driver.find_element(By.CSS_SELECTOR,"#user-name")
    time.sleep(2)
    username.send_keys(user_name_data)

    password=driver.find_element(By.CSS_SELECTOR,"#password")
    password.send_keys(password_data)
    #button_login
    login_in=driver.find_element(By.CSS_SELECTOR,"#login-button")
    login_in.click()
 


    input("type here enter for close :")


page("standard_user","secret_sauce")
