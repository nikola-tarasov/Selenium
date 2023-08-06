import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.saucedemo.com'

driver = webdriver.Firefox(executable_path='C:\\Users\\Admin\\PycharmProjects\\Selenium\\geckodriver.exe')

driver.get(url)

standart_login = "standard_use"
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


#отрицательное тестирование значения при помощи assert(сравнения)
warrning = driver.find_element(By.XPATH, "//h3[@data-test='error']")
test_warning = warrning.text
assert test_warning == 'Epic sadface: Username and password do not match any user in this service'
print('Erorr!!!')
