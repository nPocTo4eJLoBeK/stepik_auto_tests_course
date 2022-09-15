from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def sum (num1, num2):
    return str(num1 + num2)


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    y = sum(int(num1), int(num2))
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(y)
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()