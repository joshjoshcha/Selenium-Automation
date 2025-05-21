
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()


# WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.ID, cookie_id))
# )
#
# cookie = driver.find_element(By.ID, cookie_id)
# cookie.click()
#
# time.sleep(10)



# input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# input_element.clear()
# input_element.send_keys("tech with tim" + Keys.ENTER)
#
# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
# )
#
# link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
# link.click()
#
#
#
# time.sleep(10)
#
# driver.quit()