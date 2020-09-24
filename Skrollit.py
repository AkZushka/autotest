from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
input = browser.find_element_by_css_selector("#answer")
input.send_keys(y)
checkbox = browser.find_element_by_css_selector("#robotCheckbox")
checkbox.click()
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
radio = browser.find_element_by_css_selector("#robotsRule")
radio.click()
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(10)
browser.quit()

