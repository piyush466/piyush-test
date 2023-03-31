import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setuppiyush")

class TestE2e:
    def test_eee(self):
        product_lists = self.driver.find_elements(By.XPATH, '//div[@class="card h-100"]')
        for product_list in product_lists:
            print(product_list.find_element(By.XPATH, "div[1]/h4").text)
            names = product_list.find_elements(By.XPATH, "div[1]/h4")
            for name in names:
                if name.text == "Samsung Note 8":
                    product_list.find_element(By.XPATH, 'div[2]/button').click()























       # mobile = self.driver.find_elements(By.XPATH ,"//h4/a")
       # for mobil in mobile:
       #     print(mobil.text)
       #     if mobil.text == "Blackberry":
       #         self.driver.find_element(By.XPATH, "//button[@class='btn btn-info']").click()


