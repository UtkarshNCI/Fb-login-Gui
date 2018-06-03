from selenium import webdriver 
from time import sleep
from getpass import getpass

usr=input("Enter Email Id:")
pwd=getpass("Enter Password")

driver=webdriver.Chrome("C:/Users/Utkarsh/AppData/Local/Programs/Python/Python36")
driver.get("https://www.facebook.com/")
print("Opened Facebook")
sleep(1)

username=driver.find_element_by_id('email')
username.send_keys(usr)
print("Username entered")
sleep(1)

password=driver.find_element_by_id('password')
password.send_keys(pwd) 
print("Password entered")
sleep(1)

login_click=driver.find_element_by_id("loginbutton")
login_click.click()


print("All Done")
input("if sucessfull input anything")
driver.quit()
print("Finished")