from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    username_name = "email"
    passweord_id = "password"
    submit_Xpath = "//*[@id='registration']/div[4]/div[1]/button"

    def __init__(self,driver):
        self.driver =driver


    def setusername(self,username):
        self.driver.find_element(By.NAME,self.username_name).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID,self.passweord_id).send_keys(password)

    def clicksubmit(self):
        self.driver.find_element(By.XPATH,self.submit_Xpath).click()


