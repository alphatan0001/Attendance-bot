# -*- coding: utf-8 -*-
from IDPASS import ID
from IDPASS import Password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Attendance Automation\Chromedriver\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://lms.rgukt.ac.in/")
        #driver.maximize_window()
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(ID)
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(Password)
        driver.find_element_by_id("loginbtn").click()
        driver.find_element_by_link_text("Elements of Mechanical Engineering").click()
        driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", driver.find_element_by_link_text("Attendance"))
        driver.find_element_by_link_text("Attendance").click()
        element = driver.find_element_by_class_name("footer")
        driver.execute_script("""
                        var element = arguments[0];
                        element.parentNode.removeChild(element);
                        """, element)
        driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", driver.find_element_by_link_text("Submit attendance"))
        driver.find_element_by_link_text("Submit attendance").click()
        driver.find_element_by_id("id_status_1935").click()
        driver.find_element_by_id("id_submitbutton").click()
    
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
