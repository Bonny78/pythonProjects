from selenium import webdriver
import time

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver =webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        #Depending on location, might have to accept the GDPR pop-up
        #accept_button =driver.find_element_by_id("_evidon-banner-acceptbutton")
        #accept_button.click()

        time.sleep(7)
        go_button = self.driver.find_element_by_css_selector(".start-button .start-text")
        go_button.click()

        time.sleep(80)
        speed_down = self.driver.find_element_by_css_selector(".result-item-download .result-data-large")
        self.down = float(speed_down.text)

        speed_up = self.driver.find_element_by_css_selector(".result-item-upload .result-data-large")
        self.up = float(speed_up.text)

    def tweet_at_provider(self, username, password, promised_down, promised_up, provider):
        self.driver.get("https://twitter.com/?lang=en")
        time.sleep(3)
        login = self.driver.find_element_by_xpath(
            "//div[@id='react-root']/div/div/div/main/div/div/div/div/div/div[3]/a[2]/div").click()

        time.sleep(3)
        user_name = self.driver.find_element_by_xpath("//input[@name='session[username_or_email]']").send_keys(
            username)
        password = self.driver.find_element_by_css_selector(".css-1dbjc4n:nth-child(7) .r-30o5oe").send_keys(password)
        login2 = self.driver.find_element_by_css_selector(".r-1fz3rvf > .css-901oao").click()

        complaint = f"Hey {provider}! Why is my speed {self.down}down/{self.up}up when I pay for {promised_down}down/{promised_up}up"
        time.sleep(5)
        write_complain = self.driver.find_element_by_css_selector(".DraftEditor-editorContainer div").send_keys(complaint)
        tweet_button = self.driver.find_element_by_css_selector(".r-19u6a5r > .css-901oao").click()

        time.sleep(2)
        self.driver.quit()


