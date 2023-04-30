import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# This is a class that sets up a webdriver for Edge browser using the unittest module in Python.
class using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path=r'C:\DriverEdge\msedgedriver.exe')

    def test_using_toggle(self):
        """
        The function tests the functionality of a toggle switch on a web page using Selenium WebDriver.
        """
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_css_switch.asp')
        time.sleep(3)
        toggle_push = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[1]/label[3]/div')
        toggle_push.click()
        time.sleep(3)
        toggle_push.click()
        time.sleep(3)

    def tearDown(self):
        """
        The function `tearDown` closes the driver in a Python test case.
        """
        self.driver.close()
if __name__ == '__main__':
    unittest.main()