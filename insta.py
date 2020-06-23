from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import sleep


class instagramPost:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("https://instagram.com")
        sleep(2)

    # Log in
    def login(self):

        # username
        username_field = self.driver.find_element_by_name("username")
        username_field.send_keys('')

        # break
        sleep(2)

        # password
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys('')

        # break
        sleep(2)

        # submit
        submit = self.driver.find_element_by_tag_name('form')
        submit.submit()

        # break
        sleep(2)

        # Notifications
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[3]/button[2]").click()

        # break
        sleep(2)


bot = instagramPost('carocode_', 'Pelusa1488!')
bot.login()
