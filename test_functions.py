import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By




#
# @pytest.mark.usefixtures("setup")
# class Test_demo:

@pytest.mark.usefixtures("setup")
class Test_he:
    def test_login(self):

        self.driver.find_element(By.CSS_SELECTOR, "#email").send_keys("piyush")
        self.driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("1234355")
        self.driver.find_element(By.ID, "loginbutton").click()
        time.sleep(4)
        msg = self.driver.find_element(By.XPATH, "//div[@class='_9ay7']").text
        print(msg)
        print(self.driver.title)
        assert msg == "The password that you've entered is incorrect. Forgotten password?", "failed test cse"





