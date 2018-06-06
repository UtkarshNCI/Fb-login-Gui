import os
from selenium import webdriver
 
chrome_path="C:/Users/Utkarsh/Downloads/chromedriver_win32/chromedriver.exe"
cwd=os.getcwd()
print(cwd)
ok=os.path.join(cwd,'chromedriver.exe')
print (ok)
k=input()
driver=webdriver.Chrome(chrome_path)
 
driver.maximize_window()
 
driver.implicitly_wait(30)
driver.get('http://www.google.com')
driver.quit()