from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(url)
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()


    x = browser.find_element(By.ID, "input_value").text
    y = calc(int(x))

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()


finally:
    time.sleep(5)
    browser.quit()

