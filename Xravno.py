from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
input = browser.find_element_by_css_selector("#answer")
input.send_keys(y)
checkbox = browser.find_element_by_css_selector("#robotCheckbox")
checkbox.click()
radio = browser.find_element_by_css_selector("#robotsRule")
radio.click()
button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(10)
browser.quit()

