# One.UF Course Registration Automation

This project automates course registration on the University of Florida's One.UF portal using Python and Selenium. It mimics user actions such as selecting classes, submitting registration, and scrolling — all while maintaining session state via Chrome's remote debugging mode.

## 🔧 Features

- Automates course registration using a real browser session
- Leverages remote debugging to reuse logged-in Chrome state
- Uses explicit waits and scroll logic to handle modals and dynamic content
- Avoids time.sleep() for speed and robustness

## 🛠 Tech Stack

- Python 3
- Selenium
- Chrome (remote debugging mode)
- `webdriver-manager`

## 🚀 How to Use

1. Launch Chrome in remote debug mode via terminal
chrome --remote-debugging-port=9222 --user-data-dir="C:/ChromeProfile"

2. Manually log in to One.UF in the new Chrome window.

3. Open another terminal and run the bot
python "UF course registration.py"

