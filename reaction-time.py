from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

s = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://humanbenchmark.com/tests/reactiontime")


driver.implicitly_wait(3)
clickAgree = driver.find_element(By.CLASS_NAME, "Button__StyledButton-a1qza5-0")
clickAgree.click()

driver.implicitly_wait(1)
click_field_blue = driver.find_element(By.CLASS_NAME, "view-splash")
click_field_blue.click()

try:
    element = WebDriverWait(driver, 10, poll_frequency=0.00000001).until(
        EC.presence_of_element_located((By.CLASS_NAME, "view-go"))
    )
finally:
    clickNow = driver.find_element(By.CLASS_NAME, "view-go")
    clickNow.click()
