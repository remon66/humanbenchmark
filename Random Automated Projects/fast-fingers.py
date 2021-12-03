from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

s = Service('chromedriver')  # CHANGE TO .exe ON WINDOWS
driver = webdriver.Chrome(service=s)
driver.get("https://10fastfingers.com/typing-test/dutch")

driver.implicitly_wait(3)
clickAgree = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
clickAgree.click()

driver.implicitly_wait(50)
changeLang = driver.find_element(By.ID, "switch-typing-test-language")
changeLang.click()

driver.implicitly_wait(2)
parentElement = driver.find_element(By.ID, "language-list")
elementList = parentElement.find_elements(By.TAG_NAME, "a")
for country in elementList:
    if country.text == "Hebrew":  # CHANGE LANGUAGE HERE
        country.click()
        break

def enterWord(word):
    inputfield = driver.find_element(By.CLASS_NAME, "form-control")
    inputfield.send_keys(word)
    inputfield.send_keys(Keys.SPACE)
    getWord()


def getWord():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "highlight"))
        )
    finally:
        word = driver.find_element(By.CLASS_NAME, "highlight")
        enterWord(word.text)


getWord()
