import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.saucedemo.com'

driver = webdriver.Firefox(executable_path='C:\\Users\\Admin\\PycharmProjects\\Selenium\\geckodriver.exe')

driver.get(url)

standart_login = "standard_user"
all_password = 'secret_sauce'

print("Вход по логину")

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(standart_login)

print("Ввод пароля")

password = driver.find_element(By.XPATH, '//input[@id="password"]')

password.send_keys(all_password)

print("Нажатие кнопки")

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()


# text_produts = driver.find_element(By.XPATH, "//span[@class='title']")
# value_text_produts = text_produts.text
# print(value_text_produts)


