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

#javascript integrated code to python-selenium
counter_for_scroll = 0
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False) and counter_for_scroll <= 5:
    counter_for_scroll += 1 
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
    
time.sleep(10)
tweets = driver.find_elements(By.CSS_SELECTOR, ".css-901oao.r-1fmj7o5.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0")

with open("Enter-Hastag-What-You-Want-To-Search.txt",'w',encoding='utf-8') as file:
    tweet_ct = 1
    for tweet in tweets:
        file.write("*************************\n")
        file.write(str(tweet_ct)+".\n"+tweet.text+"\n")
        tweet_ct += 1

time.sleep(10)
driver.close()
