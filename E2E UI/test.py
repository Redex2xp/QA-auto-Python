from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_purchase():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com')

    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    assert "Sauce Labs Backpack" in driver.page_source

    driver.find_element(By.ID, 'checkout').click()
    driver.find_element(By.ID, 'first-name').send_keys('ВашеИмя')
    driver.find_element(By.ID, 'last-name').send_keys('ВашаФамилия')
    driver.find_element(By.ID, 'postal-code').send_keys('12345')
    driver.find_element(By.ID, 'continue').click()
    driver.find_element(By.ID, 'finish').click()

    assert "Thank you for your order!" in driver.page_source

    driver.quit()

if __name__ == "__main__":
    test_purchase()
