from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    first_window = browser.window_handles[0]
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(int(x))

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = browser.switch_to.alert.text
    print(alert_text)
    alert.accept()

finally:
    browser.quit()
