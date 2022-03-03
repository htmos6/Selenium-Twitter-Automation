#set up for every selenium python script
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s = Service('C:/Users/Legion/Desktop/Python/geckodriver-v0.30.0-win64/geckodriver.exe') # enter your path of geckodriver
driver = webdriver.Firefox(service=s)
driver.maximize_window() # For maximizing window
driver.implicitly_wait(10)
#end of set up for every selenium python script

driver.get("https://twitter.com/")
login = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a")
driver.implicitly_wait(10)
login.click()

username_area = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input")
username_area.send_keys("Your-Twitter-Username-Enter-Here")
driver.implicitly_wait(10)

next_button = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div")
driver.implicitly_wait(10)
next_button.click()

password_area = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
password_area.send_keys("Your-Twitter-Password-Enter Here")
driver.implicitly_wait(10)

log_in_button = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div")
log_in_button.click()
driver.implicitly_wait(10)

search_area = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
search_area.send_keys("#Enter-Hastag-What-You-Want-To-Search")
search_area.send_keys(Keys.ENTER)
driver.implicitly_wait(10)

# integrated javascript code to python-selenium for auto scroll
counter_for_scroll = 0
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False) and counter_for_scroll <= 2:
    counter_for_scroll += 1 
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
    time.sleep(3)
    
like_elements = driver.find_elements(By.CSS_SELECTOR,'[data-testid="like"]') # like buttons can be found with data-testid="like"
driver.implicitly_wait(10)

counter_for_like = 0
for like_element in like_elements:
    if counter_for_like <= 6:
        like_element.click()
        counter_for_like += 1
    else:
        continue

driver.close()
