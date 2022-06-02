from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException

PROM_DOWN = 16
PROM_UP = 5
Chrome_driver_path = Service(executable_path= "/Users/hilmialperates/development_alper/chromedriver")
similar_account = "Some one account name"
username = "someuser name"
password = "password"

class InstaFollower():
    def __init__(self):
        self.chrome_driver = Service(executable_path="/Users/hilmialperates/development_alper/chromedriver")
    def login(self):
        self.driver = webdriver.Chrome(service=self.chrome_driver)
        self.driver.get("https://www.instagram.com/")
        time.sleep(4)
        login1 = self.driver.find_element(By.NAME, "username")
        login1.send_keys(username)
        login2 = self.driver.find_element(By.NAME, "password")
        login2.send_keys(password)
        time.sleep(1)
        login2.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(8)
        search = self.driver.find_element(By.CSS_SELECTOR, ".MWDvN input")
        search.send_keys(similar_account)
        search.send_keys(Keys.ENTER)
        time.sleep(6)
        clicking = self.driver.find_element(By.CSS_SELECTOR,".-qQT3 div" )
        clicking.click()
        time.sleep(10)
        dene = self.driver.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/div/span")
        followers_num = dene.text
        #x = followers_num.split(".")
        #print(x)
        #self.range_num = int(round(int(x[0])*1/7)-2)
        time.sleep(4)
        followers_f = self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/div")
        #followers_f = self.driver.find_element(By.CLASS_NAME, "g47SY")
        followers_f.click()

    def follow(self):
        n = 0
        time.sleep(4)
        modal = self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[2]')
        for i in range(0,5):
            all_bottons = self.driver.find_elements(By.CSS_SELECTOR,"li button")
            for botton  in all_bottons:
                    try:
                        time.sleep(1)
                        print(botton.text)
                        if botton.text != "Follow":
                            pass
                        else:
                            botton.click()
                            time.sleep(1)
                    except ElementClickInterceptedException:
                        time.sleep(1)
                        cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[7]/div/div/div/div[3]/button[2]')
                        cancel_button.click()
                    finally:
                        time.sleep(1)
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
ista_follow = InstaFollower()
login = ista_follow.login()
followers = ista_follow.find_followers()
follow = ista_follow.follow()



