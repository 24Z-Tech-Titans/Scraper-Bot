import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with

url = "https://www.airbnb.com/"

class Driver:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.login()
        
    def login(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@data-testid='cypress-headernav-profile']")))
        login_icon = self.driver.find_element(By.XPATH, "//*[@data-testid='cypress-headernav-profile']")
        login_icon.click()
        login_btn = self.driver.find_element(locate_with(By.TAG_NAME, "a").below(login_icon))
        login_btn.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@data-testid='social-auth-button-email']")))
        email_login_btn = self.driver.find_element(By.XPATH, "//*[@data-testid='social-auth-button-email']")
        email_login_btn.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@data-testid='email-login-email']")))
        email_input = self.driver.find_element(By.XPATH, "//*[@data-testid='email-login-email']")
        email_input.send_keys("ki.keter@lightacademy.ac.ke")
        continue_btn = self.driver.find_element(By.XPATH, "//*[@data-testid='signup-login-submit-btn']")
        continue_btn.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@data-testid='email-signup-password']")))
        password_input = self.driver.find_element(By.XPATH, "//*[@data-testid='email-signup-password']")
        password_input.send_keys("K1234567890k")
        password_btn = self.driver.find_element(By.XPATH, "//*[@data-testid='signup-login-submit-btn']")
        password_btn.click()
        time.sleep(12)
        
scrape = Driver(url)