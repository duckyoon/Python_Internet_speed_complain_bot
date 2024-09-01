from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 500
PROMISED_UP = 500

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PWD = os.getenv("TWITTER_PWD")

twitter_url = "https://x.com/home"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        # self.driver = webdriver.get(twitter_url)

        self.down = 0
        self.up = 0
        
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(120)
        print("2m passed")
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.down, self.up)
        
    def tweet_at_provider(self):
        self.driver.get('https://x.com/')
        time.sleep(2)
        login = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div')
        login.click()
        time.sleep(1)
        input_id = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        input_id.click()
        input_id.send_keys("yunoli6")
        time.sleep(1)
        
        id_next = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        id_next.click()
        time.sleep(1)
        
        # input_email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        # input_email.click()
        # input_email.send_keys(TWITTER_EMAIL)
        # time.sleep(1)
        # email_next = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        # email_next.click()
        # time.sleep(1)
        
        
        input_pwd = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        input_pwd.click()
        input_pwd.send_keys(TWITTER_PWD)
        time.sleep(1)
        
        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login_button.click()
        time.sleep(3)
        
        input_text = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        input_text.click()
        msg = f"Internet Spped {self.down}down/{self.up}up when promises {PROMISED_DOWN}down/{PROMISED_UP}up"
        input_text.send_keys(msg)
        
        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div')
        post.click()
        
       
        pass

