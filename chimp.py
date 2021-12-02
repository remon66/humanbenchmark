from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

s = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://humanbenchmark.com/tests/chimp")

driver.implicitly_wait(3)
clickAgree = driver.find_element(By.CLASS_NAME, "Button__StyledButton-a1qza5-0")
clickAgree.click()

driver.implicitly_wait(1)
click_button = driver.find_element(By.CLASS_NAME, "css-de05nr")
click_button.click()


def do_chimp(texts):
    count = 1
    while True:
        for button in texts:
            try:
                print(button.text)
            except:
                return

            if button.text != "":
                if int(button.text) == count:
                    button.click()
                    count += 1


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "css-19b5rdt"))
    )
finally:
    count = 1
    texts = driver.find_elements(By.CLASS_NAME, "css-19b5rdt")

    do_chimp(texts)
    # WHILE... wait for continue button to appear, than do_chimps again
