# Every time before you run your script, just do this:
# pkill -f "Google Chrome"

# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
# --remote-debugging-port=9222 \
# --user-data-dir="$HOME/oneuf-bot-profile"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

# Connect to the debug-mode Chrome instance
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver, 15)

# Switch to the tab with One.UF loaded
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "one.uf.edu" in driver.current_url:
        print("✅ Switched to One.UF tab:", driver.current_url)
        break

# Click the "Register / View Schedule" button
register_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/myschedule"]')))
register_btn.click()
print("🖱️ Clicked 'Register / View Schedule'")

# Click only the "View Schedule" button for Fall 2025
fall_schedule_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="View Schedule for Fall 2025"]')))
fall_schedule_btn.click()
print("🖱️ Clicked 'View Schedule for Fall 2025'")

# Click the "+ Add Course" button (to go to the registration search)
add_course_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="Add course"]')))
add_course_btn.click()
print("➕ Clicked '+ Add Course'")

# Type "HNG1130" into the Course # box
course_input = wait.until(EC.presence_of_element_located((By.ID, "course-number")))
course_input.send_keys("HNG1130")
print("⌨️ Typed 'HNG1130' into Course # box")

# Click the Search button
search_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Search"]')))
search_btn.click()
print("🔍 Clicked 'Search'")

# Click the "+ Add Class" button for class 19430
add_class_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Add class 19430"]')))
add_class_btn.click()
print("➕ Clicked '+ Add Class' for 19430")

# Click the final "Add" button to confirm registration
final_add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Add"]')))
final_add_btn.click()
print("✅ Clicked final 'Add' to confirm registration")

# Go back to the main View Schedule screen
view_schedule_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="View Schedule"]')))
view_schedule_btn.click()
print("🔁 Clicked 'View Schedule' to return to main screen")
