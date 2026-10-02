from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


# Variables and Constants
URL = (
    "https://app.100daysofpython.dev/services/tindog/u/RlIfLvRGLdwhzKQ0eDWTxvNJiW5YKWic"
)
USERNAME = "myemail@gmail.com"
PASSWORD = "facebarkpassword"


def tindog_login():
    print("Logging in to Tindog")

    # Initialize Chrome Options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("detach", True)

    # Set up the WebDriver
    driver = webdriver.Chrome(options=options)
    try:
        # Click the Login Button
        driver.get(URL)
        login_button = driver.find_element(By.CSS_SELECTOR, value="button[class]")
        login_button.click()

        # Click on Login with FACEBARK button
        time.sleep(2)
        facebark_button = driver.find_element(
            By.XPATH, value="/html/body/div[1]/div/div/div/button[1]"
        )
        facebark_button.click()

        # Switch to the Facebark popup login window
        fb_login_window = driver.window_handles[1]
        base_window = driver.window_handles[0]
        driver.switch_to.window(fb_login_window)

        # Log in to Facebark
        username_box = driver.find_element(By.ID, "email")
        username_box.send_keys(USERNAME)
        password_box = driver.find_element(By.ID, value="pass")
        password_box.send_keys(PASSWORD)
        login_button = driver.find_element(
            By.XPATH, value="/html/body/div[2]/div/form/button"
        )
        login_button.click()

        # Switch back to Tindog Window and Allow Tindog to use my location
        driver.switch_to.window(base_window)
        allow_button = driver.find_element(By.CLASS_NAME, value="btn-primary")
        allow_button.click()

        # Fuck notifications

    except Exception as e:
        print(f"An error has occured during execution: {e}")


if __name__ == "__main__":
    tindog_login()
