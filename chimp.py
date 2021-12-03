import platform

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if "windows" in platform.platform().lower():
    s = Service('chromedriver.exe')
else:
    s = Service('chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://humanbenchmark.com/tests/chimp")

if "windows" in platform.platform().lower():
    try:
        element = WebDriverWait(driver, 100, poll_frequency=0.000001).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "Button__StyledButton-a1qza5-0"))
        )
    finally:
        clickAgree = driver.find_elements(By.CLASS_NAME, "Button__StyledButton-a1qza5-0")
        clickAgree[1].click()
        clickAgree[0].click()
    try:
        element = WebDriverWait(driver, 100, poll_frequency=0.00001).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-de05nr"))
        )
    finally:
        click_button = driver.find_element(By.CLASS_NAME, "css-de05nr")
        click_button.click()
else:
    clickAgree = driver.find_element(By.CLASS_NAME, "Button__StyledButton-a1qza5-0")
    clickAgree.click()

    click_button = driver.find_element(By.CLASS_NAME, "css-de05nr")
    click_button.click()


def do_chimp():
    count = 1
    while True:
        texts = driver.find_elements(By.CSS_SELECTOR, "[data-cellnumber='" + str(count) + "']")
        if not texts:
            continueHere()
            break
        for button in texts:
            print(button.text)
            try:
                print(button.text)
            except:
                print("null")

            if button.text != "":
                if button.text != '.' and button.text == str(count):
                    button.click()
                    count += 1
                elif button.text == '.' and button.get_attribute('data-cellnumber') == str(count):
                    button.click()
                    count += 1


def continueHere():
    try:
        element = WebDriverWait(driver, 10, poll_frequency=0.00001).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-de05nr"))
        )
    finally:
        continueButton = driver.find_element(By.CLASS_NAME, "css-de05nr")
        continueButton.click()
        print("done")
        do_chimp()


while True:
    try:
        element = WebDriverWait(driver, 10, poll_frequency=0.00001).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-cellnumber='1']"))
        )
    finally:
        count = 1
        texts = driver.find_elements(By.CSS_SELECTOR, "[data-cellnumber='" + str(count) + "']")
        print("top")
        do_chimp()
