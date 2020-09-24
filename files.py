from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element_by_css_selector('[name="firstname"]')
input1.send_keys("Andrey")
input2 = browser.find_element_by_css_selector('[name="lastname"]')
input2.send_keys("Zavisnov")
input3 = browser.find_element_by_css_selector('[name="email"]')
input3.send_keys("azavisnov@dadaya.com")
with open("test.txt", "w") as file:
    file.write("yesitis")
path = os.getcwd() + '/' + file.name
element = browser.find_element_by_css_selector("#file")
element.send_keys(path)
button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(1)
time.sleep(10)
browser.quit()

