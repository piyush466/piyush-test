# <<<<<<< HEAD
# import pytest as pytest
# from selenium import webdriver
#
# @pytest.fixture
# def setup():
#     option1 = webdriver.ChromeOptions()
#     option1.add_argument("--start-maximized")
#     driver = webdriver.Chrome(chrome_options=option1)
#     print("your chrome driver is launching")
#     return driver
# =======
# import time
#
# import pytest

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
#
# @pytest.fixture(scope="class")
# def setuppiyush(request):
#     obj_ser = Service()
#     driver = webdriver.Chrome(service=obj_ser)
#     driver.get("https://rahulshettyacademy.com/angularpractice/shop")
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     time.sleep(15)
#     driver.close()
#
#
#
#
#
# >>>>>>> d9d99907f72afaefe2a86691fe4ed30766473043
