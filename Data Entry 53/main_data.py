import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSeQrTQgIsp68IwIMie5sXS61LE8k0o_5U5yYPhUE7Dzi3w10w/viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
chrome_driver_path = "C:\Development\chromedriver.exe"

header = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
}
response  = requests.get(ZILLOW_URL, headers=header)
zillow_webpage = response.text

soup =BeautifulSoup(zillow_webpage, "html.parser")

list_of_links = soup.select(".list-card-top a")
all_links = []
for link in list_of_links:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

#Getting the list of addresses
list_of_address = soup.select(".list-card-info address")
all_addresses = []
for address in list_of_address:
    ad = address.getText()
    all_addresses.append(ad)
print(all_addresses)

#Scrape prices per month
prices = soup.select(".list-card-price")
all_prices = []
for p in prices:
    p_text = p.getText().split("+")[0]
    p_text2 = p_text.split("/mo")[0]
    print(p_text2)
    all_prices.append(p_text2)
print(all_prices)
print(len(all_addresses))
print(len(all_prices))
print(len(all_links))

#Use Selenium to fill in the form
driver =webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(FORM_LINK)
time.sleep(2)

#Fill out the goole form
for n in range(len(all_links)):
    time.sleep(6)
    address_fill =driver.find_element_by_css_selector(".freebirdFormviewerViewNumberedItemContainer:nth-child(1) .quantumWizTextinputPaperinputInput").send_keys(all_addresses[n])
    price_fill = driver.find_element_by_css_selector(".freebirdFormviewerViewNumberedItemContainer:nth-child(2) .quantumWizTextinputPaperinputInput").send_keys(all_prices[n])
    link_fill = driver.find_element_by_css_selector(".freebirdFormviewerViewNumberedItemContainer:nth-child(3) .quantumWizTextinputPaperinputInput").send_keys(all_links[n])
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()
    time.sleep(4)
    another_response_button = driver.find_element_by_css_selector(".freebirdFormviewerViewResponseLinksContainer a").click()
