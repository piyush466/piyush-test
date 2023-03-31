import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setuppiyush(request):
    obj_ser = Service()
    driver = webdriver.Chrome(service=obj_ser)
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    time.sleep(15)
    driver.close()





