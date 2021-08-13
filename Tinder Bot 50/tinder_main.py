import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


EMAIL = os.environ['email']
PASSWORD = os.environ['password']
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")

time.sleep(2)
login = driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
time.sleep(3)
fb_login = driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()

#to get to facebook window
time.sleep(2)
base_window =driver.window_handles[0]
fb_login_window =driver.window_handles[1]
#switch our Selenium to target the new Fb login window
driver.switch_to.window(fb_login_window)
#to verify its the Fb window
print(driver.title)
time.sleep(5)
fb_email =driver.find_element_by_css_selector("#email_container input").send_keys(EMAIL)
fb_pass = driver.find_element_by_xpath('//*[@id="pass"]').send_keys(PASSWORD)
fb_login2 = driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

print(driver.title)
time.sleep(3)
# driver.find_element_by_name("__CONFIRM__").click()

#driver.switch_to.window(fb_login_window2)
# driver.find_element_by_xpath('//*[@id="u_0_4_2b"]/div[2]/div[1]/div[2]/div[1]/button').click()

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5secs to allow page to laod
time.sleep(5)
#Allow location
allow_location_button = driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/div/div/div[3]/button[1]').click()
time.sleep(2)
#allow cookies
cookies_button =driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[2]/div/div/div[1]/button').click()
#disallow notifications
notification_button =driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/div/div/div[3]/button[2]').click()

time.sleep(3)

#On the free tier, Tinder only allows 100 "Likes" per day.
for reject in range(10):
    #adding 1 sec delay bewteen likes
    time.sleep(5)

    try:
        print("called dislike")
        #reject button
        reject_button = driver.find_element_by_css_selector(".Mx\(a\):nth-child(2) path")
        reject_button.click()
        time.sleep(2)
        print("liked")
        like_button = driver.find_element_by_xpath("//div[@id='c2094796203']/div/div/div/main/div/div/div/div/div/div/div[5]/div/div[4]/button/span/span")
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsMatch a")
            match_popup.click()
        #catches the case like button has yet loaded, so wait 2 secs before trying
        except NoSuchElementException:
            time.sleep(2)

driver.quit()