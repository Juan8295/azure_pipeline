# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddEditTest(unittest.TestCase):
    def setUp(self):
        #chrome_options = Options()
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--disable-dev-shm-usage')
        s = Service("/home/azureuser/Downloads/chromedriver",)
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8084/petclinic"
        self.verificationErrors = []
        self.accept_next_alert = True
    # the first test is to add a new owner
    def test_add_edit(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1848,1007 | ]]
        driver.get("http://localhost:8084/petclinic/owners/find")
        driver.find_element(By.CSS_SELECTOR,"a[title=\"find owners\"]").click()
        driver.find_element(By.LINK_TEXT,"Add Owner").click()
        driver.find_element(By.ID,"firstName").click()
        driver.find_element(By.ID,"firstName").clear()
        driver.find_element(By.ID,"firstName").send_keys("Juan")
        driver.find_element(By.ID,"lastName").clear()
        driver.find_element(By.ID,"lastName").send_keys("Goez Cordoba")
        driver.find_element(By.ID,"address").clear()
        driver.find_element(By.ID,"address").send_keys("Paasheuevelweg 3")
        driver.find_element(By.ID,"address").send_keys(Keys.DOWN)
        driver.find_element(By.ID,"address").send_keys(Keys.TAB)
        driver.find_element(By.ID,"address").clear()
        driver.find_element(By.ID,"address").send_keys("Paasheuevelweg 3")
        driver.find_element(By.ID,"city").clear()
        driver.find_element(By.ID,"city").send_keys("Amsterdam")
        driver.find_element(By.ID,"telephone").clear()
        driver.find_element(By.ID,"telephone").send_keys("0612345678")
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()
    #second test is to add new pets     
        driver.find_element(By.LINK_TEXT,"Add New Pet").click()
        driver.find_element(By.ID,"name").click()
        driver.find_element(By.ID,"name").clear()
        driver.find_element(By.ID,"name").send_keys("lupi")
        driver.find_element(By.ID,"birthDate").click()
        driver.find_element(By.LINK_TEXT,"10").click()
        Select(driver.find_element(By.ID,"type")).select_by_visible_text("dog")
        driver.find_element(By.CSS_SELECTOR,"option[value=\"dog\"]").click()
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()
    # 3e is to test "edit owner"
        driver.find_element(By.LINK_TEXT,"Edit Owner").click()
        driver.find_element(By.ID,"firstName").click()
        driver.find_element(By.ID,"firstName").clear()
        driver.find_element(By.ID,"firstName").send_keys("Juan Camilo")
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()
        driver.find_element(By.XPATH,"//div[@id='main-navbar']/ul/li[3]/a/span[2]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
