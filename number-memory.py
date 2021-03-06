
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

if "windows" in platform.platform().lower():
    s = Service('chromedriver.exe')
else:
    s = Service('chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://humanbenchmark.com/tests/number-memory")

if "windows" in platform.platform().lower():
    try:
        element = WebDriverWait(driver, 100).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "Button__StyledButton-a1qza5-0"))
        )
    finally:
        driver.implicitly_wait(3)
        clickAgree = driver.find_elements(By.CLASS_NAME, "Button__StyledButton-a1qza5-0")
        clickAgree[1].click()
        driver.implicitly_wait(2)
        clickAgree[0].click()
    try:
        element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-de05nr"))
        )
    finally:
        click_button = driver.find_element(By.CLASS_NAME, "css-de05nr")
        click_button.click()
else:
    driver.implicitly_wait(3)
    clickAgree = driver.find_element(By.CLASS_NAME, "Button__StyledButton-a1qza5-0")
    clickAgree.click()

    driver.implicitly_wait(10)
    click_button = driver.find_element(By.CLASS_NAME, "css-de05nr")
    click_button.click()

count = 0


def enterNumber(number):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[type=text]"))
        )
    finally:
        inputField = driver.find_element(By.CSS_SELECTOR, "[type=text]")
        driver.implicitly_wait(1)
        inputField.send_keys(number)
        driver.implicitly_wait(1)
        inputField.send_keys(Keys.ENTER)
        continueHere()


def continueHere():
    global count
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-de05nr"))
        )
    finally:
        continueButton = driver.find_element(By.CLASS_NAME, "css-de05nr")
        continueButton.click()
        count += 1
        print("Level " + str(count))
        getNumber()


def getNumber():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "big-number"))
        )
    finally:
        number = driver.find_element(By.CLASS_NAME, "big-number")
        enterNumber(number.text)


getNumber()
