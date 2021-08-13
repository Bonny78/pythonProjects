import os
from internet_speed_twitter_bot import InternetSpeedTwitterBot

TWITTER_USERNAME =os.environ['username']
TWITTER_PASS = os.environ['password']
PROMISED_UP = 10
PROMISED_DOWN = 150
INTERNET_PROVIDER = "Internet Provider"
chrome_driver_path = "C:\Development\chromedriver.exe"

#Creting Internet Speed check bot
bot =InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
speed_up = bot.up
speed_down = bot.down
print(bot.up)
print(bot.down)

#if speed up or down lower than promised than complain
if speed_up < PROMISED_UP or speed_down < PROMISED_DOWN:
    #making the bot tweet complain in Tweeter
    bot.tweet_at_provider(TWITTER_USERNAME, TWITTER_PASS, PROMISED_DOWN, PROMISED_UP, INTERNET_PROVIDER)