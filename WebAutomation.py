import os
import datetime
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Vendors import vendors

username = os.getlogin()

path = f"C:\\Users\{username}\Desktop\RSPO-SCC-Review-Public-Main\msedgedriver.exe"
PATH = path


driver = webdriver.Edge(PATH)

now = datetime.datetime.now()


original_path = (f"C:\\Users\{username}\Desktop\RSPO-SCC-Review-Public")
folder_date = str(now.strftime("%Y-%m-%d"))
new_path = original_path+'\\'+folder_date

if not os.path.exists(new_path):
    os.mkdir(new_path)
    print("Created Directory")
else:
    print("Directory already existed")
                             

for vendor in vendors:
    driver.get("https://rspo.secure.force.com/membership/RSPOSCCSearch")
    driver.maximize_window()
    driver.implicitly_wait(5)
    search = driver.find_element("id", "j_id0:j_id51:input-keyword")
    search.send_keys(vendor)
    search.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)
    status = driver.find_element("id","j_id0:searchresults:0:j_id100")
    pyautogui.screenshot().save(new_path+'\\'+vendor+'.png')
    print(vendor, "is", status.text, "as of", now.strftime("%Y-%m-%d %H:%M:%S"))
driver.implicitly_wait(5)
driver.close()
    
    
