import pytest as pytest
from selenium import webdriver

@pytest.fixture
def setup():
    option1 = webdriver.ChromeOptions()
    option1.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=option1)
    print("your chrome driver is launching")
    return driver