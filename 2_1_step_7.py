from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")

    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio_button = browser.find_element(By.ID, "robotsRule")
    radio_button.click()

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()