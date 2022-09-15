from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

url = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    firstname = browser.find_element(By.NAME, "firstname")
    firstname.send_keys("1")

    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("1")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("1")

    add_file = browser.find_element(By.ID, "file")
    file = open("file.txt", "w")
    file.close()
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')
    add_file.send_keys(file_path)
    os.remove("file.txt")

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()