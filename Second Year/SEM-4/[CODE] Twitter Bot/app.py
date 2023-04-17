from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/i/flow/login')
        time.sleep(5)
        email = bot.find_element(By.NAME, 'text')
        email.send_keys(self.username)
        email.send_keys(Keys.RETURN)
        time.sleep(3)
        password = bot.find_element(By.NAME, 'password')
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

ed = TwitterBot('avskdkpro@gmail.com', 'Kdk@1303200311102003')
ed.login()