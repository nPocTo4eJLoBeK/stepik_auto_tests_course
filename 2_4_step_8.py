from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(url)
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"),
                                                                               "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(int(x))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()
    alert = browser.switch_to.alert
    text = alert.text
    alert.accept()
finally:
    print(text)
    browser.quit()