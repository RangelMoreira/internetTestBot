import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:

    def __init__(self):
        load_dotenv()
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.promise_up = os.getenv('PROMISE_UP')
        self.promise_down = os.getenv('PROMISE_DOWN')
        self.twitter_username = os.getenv('TWITTER_USERNAME')
        self.twitter_pass = os.getenv('TWITTER_PASSWORD')
        self.url_speedtest = "https://www.speedtest.net/"
        self.url_twitter = "https://x.com/i/flow/login"

    def get_internet_speed(self):
        try:
            self.driver.get(self.url_speedtest)

            go_button = self.driver.find_element(by=By.CLASS_NAME, value='js-start-test')
            go_button.click()

            time.sleep(90)

            download_speed = self.driver.find_element(by=By.CLASS_NAME, value='download-speed')
            print(f"Download {download_speed.text}")

            upload_speed = self.driver.find_element(by=By.CLASS_NAME, value='upload-speed')
            print(f"Upload {upload_speed.text}")

            message = (f"Hey Internet Provider, why is my "
                       f"internet speed {download_speed.text}down/{upload_speed.text}up when I pay for 150down/10up?")

            return message
        except NoSuchElementException:
            raise NoSuchElementException

    def tweet_at_provider(self, speed_message):
        try:
            self.driver.get(self.url_twitter)
            time.sleep(5)

            # Email
            xpath_email ='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label'
            txt_username = self.driver.find_element(By.XPATH, xpath_email)
            txt_username.send_keys(self.twitter_username)

            # "Advance Button"
            xpath_advance_button ='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]'
            bt_advance = self.driver.find_element(By.XPATH,xpath_advance_button)
            bt_advance.click()

            time.sleep(2)

            # Password
            xpath_pass = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label'
            txt_pass = self.driver.find_element(By.XPATH, xpath_pass)
            txt_pass.send_keys(self.twitter_pass)

            xpath_enter_button = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button'
            bt_enter = self.driver.find_element(By.XPATH, xpath_enter_button)
            bt_enter.click()

            time.sleep(5)

            # Message
            xpath_tweet = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
            txt_tweet = self.driver.find_element(By.XPATH, xpath_tweet)
            txt_tweet.send_keys(speed_message)

            # Post Button
            xpath_post_button = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button'
            bt_post = self.driver.find_element(By.XPATH, xpath_post_button)
            bt_post.click()

        except NoSuchElementException:
            raise NoSuchElementException
