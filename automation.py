from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    service = Service('chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    url = 'https://demo.seleniumeasy.com/basic-first-form-demo.html'
    driver.get(url)

    show_message_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
    assert 'Show Message' in driver.page_source

    user_message = driver.find_element(By.ID, 'user-message')
    user_message.clear()
    user_message.send_keys('Hello there!... General Kenobi')
    show_message_button.click()

    message_display = driver.find_element(By.ID, 'display')

    assert 'Hello there!... General Kenobi' in message_display.text
