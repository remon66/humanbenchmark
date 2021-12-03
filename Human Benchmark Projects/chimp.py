from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

s = Service('chromedriver')  # CHANGE TO .exe ON WINDOWS
driver = webdriver.Chrome(service=s)
driver.get("https://humanbenchmark.com/tests/chimp")

driver.implicitly_wait(3)
clickAgree = driver.find_element(By.CLASS_NAME, "Button__StyledButton-a1qza5-0")
clickAgree.click()

driver.implicitly_wait(1)
click_button = driver.find_element(By.CLASS_NAME, "css-de05nr")
click_button.click()


def do_chimp():
    count = 1
    while True:
        texts = driver.find_elements(By.CSS_SELECTOR, "[data-cellnumber='" + str(count) + "']")
        print(texts)
        if not texts:
            continueHere()
            break
        for button in texts:
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
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-de05nr"))
        )
    finally:
        continueButton = driver.find_element(By.CLASS_NAME, "css-de05nr")
        continueButton.click()
        print("done")
        do_chimp()


while True:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-cellnumber='1']"))
        )
    finally:
        count = 1
        texts = driver.find_elements(By.CSS_SELECTOR, "[data-cellnumber='" + str(count) + "']")
        print("top")
        do_chimp()
