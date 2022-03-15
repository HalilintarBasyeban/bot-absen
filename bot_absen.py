from lib2to3.pgen2 import driver
from selenium import webdriver
import pyautogui
import time


#your username and password
username="#"
password="#"

#the url that you want to go
url="#"

#locate the web driver on your device
driver = webdriver.Chrome(r"#")

#get the url that we already describe before
driver.get(url)

#find the element from inspect element on chrome developer mode
driver.find_element_by_name("email").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_class_name("btn").submit()

#full screen windows
driver.maximize_window()

#after login success, the page will go in here
driver.get("#")


'''
Optional
#choose time work & input work detail
time="08.00 - 17.00"
work_detail="Mengerjakan Task Daily"

#choose time shift and input the text box
driver.find_element_by_name("#").send_keys(time)
driver.find_element_by_class_name("#").send_keys(work_detail)

#the button will wait 10 second and then clicked
time.sleep(10)
driver.find_element_by_id("#").click()
'''