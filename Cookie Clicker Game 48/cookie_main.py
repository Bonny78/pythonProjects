from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#get cookie to click on
cookie =driver.find_element_by_id("cookie")

time_out = time.time() + 5
five_min = time.time() + 60*5

#get upgrade item ids
items = driver.find_elements_by_css_selector("#store div")
items_ids = [i.get_attribute("id") for i in items]
print(items_ids)

game_on =True
while game_on:
    cookie.click()

    #Every 5 secs
    if time.time() > time_out:
       #Get all upgrade <b> tags
       all_prices = driver.find_elements_by_css_selector("#store b")
       item_prices = []

       #Convert <b> text into integer price
       for price in all_prices:
           price_text = price.text
           if price_text != "":
               cost = int(price_text.split("-")[1].strip().replace(",", ""))
               item_prices.append(cost)
       print(item_prices)

       #Create dictionary of store items and ids
       cookie_upgrades ={}
       for n in range(len(item_prices)):
           cookie_upgrades[item_prices[n]] = items_ids[n]

       #Get current cookie count
       cookie_count_text = driver.find_element_by_id("money").text
       if "," in cookie_count_text:
           cookie_count_text = cookie_count_text.replace(",","")
       cookie_count_int =int(cookie_count_text) #convert count to int

       # Finding upgrades we can afford
       affordable_upgrades ={}
       for costs, ids in cookie_upgrades.items():
           if cookie_count_int > costs:
               affordable_upgrades[costs] = ids

       #Purchase the most expensive upgrade
       highest_price_affordable_upgrdade = max(affordable_upgrades)
       print(highest_price_affordable_upgrdade)
       purchase_id = affordable_upgrades[highest_price_affordable_upgrdade] #gets the id to click on upgrade

       #Click the most expensive upgrade
       driver.find_element_by_id(purchase_id).click()

       #Adding another 5sec until next check
       time_out = time.time() + 5

    #After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second"
    if time.time() > five_min:
        cookie_per_sec =driver.find_element_by_id("cps").text
        print(f"My cookie per sec is: {cookie_per_sec}")
        game_on =False
        driver.quit() #This closes the window and prints our cps
        break