from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
delay_to_load_page = 10  # seconds
import time

login_username = 'Admin'
login_password = 'admin123'

shift_name = 'somethink'
minsal = '1'
maxsal = '1000'


class GradestTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def login_page(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//input[@name="username"]'))).send_keys(login_username)
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(login_password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
                (By.XPATH, '//span[text()="Admin"]'))).click()

    def main_page(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
                (By.XPATH, '//span[contains(text(),"Job")]'))).click()
        self.driver.find_element(By.XPATH, '//a[contains(text(),"Pay Grades")]').click()

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
                (By.XPATH, '//button[contains(.,"Add")]'))).click()

    def add_salary(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
                (By.XPATH, '//input[not(@placeholder)]'))).send_keys(shift_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//button[contains(.,"Save")]').click()

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//button[contains(.," Add ")]'))).click()
        time.sleep(2)
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//div[@class="oxd-select-text-input"]'))).click()
        time.sleep(2)
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//span[contains(text(),"AED")]'))).click()
        time.sleep(2)

        MinXpath = f'/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/div/div[2]/input'
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, MinXpath))).send_keys(minsal)
        time.sleep(2)
        MaxXpath = f'/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/div[2]/input'
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, MaxXpath))).send_keys(maxsal)
        time.sleep(2)
        buttonSave = f'/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[3]/button[2]'
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, buttonSave))).click()

    def check_new_Currency(self):
        xpath_found_row = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "10.00")]'
        found_row = WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, xpath_found_row)))

        found_row.find_element(By.XPATH, '//div[contains(., "1.00")]')
        found_row.find_element(By.XPATH, '//div[contains(., "1000.00")]')

    def remove_currency(self):
        DeleteButton = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "10.00")]//i[@class="oxd-icon bi-trash"]'
        found_Currency = self.driver.find_element(By.XPATH, DeleteButton)
        time.sleep(3)
        found_Currency.find_element(By.XPATH, '//i[@class="oxd-icon bi-trash"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//button[contains(.,"Yes, Delete")]').click()
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, DeleteButton)
            assert 'Grades not removed'
        except NoSuchElementException:
            pass

    def delete_grades(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//button[contains(.,"Cancel")]'))).click()
        time.sleep(3)
        DeleteButton = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "{shift_name}")]//i[@class="oxd-icon bi-trash"]'
        self.driver.find_element(By.XPATH, DeleteButton).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//button[contains(.,"Yes, Delete")]').click()
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, DeleteButton)
            assert 'Element not removed'
        except NoSuchElementException:
            pass

        self.driver.close()
