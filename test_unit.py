import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element_by_xpath('html/body/div/form/div/div[label[contains(text(), "First name*")]]/input')
        input1.send_keys("Andrey")
        input2 = browser.find_element_by_xpath('html/body/div/form/div/div[label[contains(text(), "Last name*")]]/input')
        input2.send_keys("Zavisnov")
        input3 = browser.find_element_by_xpath('html/body/div/form/div/div[label[contains(text(), "Email*")]]/input')
        input3.send_keys("azavisnov@dadaya.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be congratulations 1 case")
        
    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element_by_xpath('html/body/div/form/div/div[label[contains(text(), "First name*")]]/input')
        input1.send_keys("Andrey")
        input2 = browser.find_element_by_xpath('html/body/div/form/div/div[label[contains(text(), "Last name*")]]/input')
        input2.send_keys("Zavisnov")
        input3 = browser.find_element_by_xpath('html/body/div/form/div/div[label[contains(text(), "Email*")]]/input')
        input3.send_keys("azavisnov@dadaya.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be congratulations 2 case")

if __name__ == "__main__":
    unittest.main()