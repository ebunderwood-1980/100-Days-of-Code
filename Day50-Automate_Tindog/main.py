from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException 


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
        print("Logged in to Tindog")

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
        print("Logging in to Facebark")
        username_box = driver.find_element(By.ID, "email")
        username_box.send_keys(USERNAME)
        password_box = driver.find_element(By.ID, value="pass")
        password_box.send_keys(PASSWORD)
        login_button = driver.find_element(
            By.XPATH, value="/html/body/div[2]/div/form/button"
        )
        login_button.click()
        print("Log in to Facebark Complete")

        # Switch back to Tindog Window and Allow Tindog to use my location
        time.sleep(2)
        driver.switch_to.window(base_window)
        allow_button = driver.find_element(By.CLASS_NAME, value="btn-primary")
        allow_button.click()

        # Fuck notifications
        not_interested_btn = driver.find_element(By.CLASS_NAME, value="btn-secondary")
        not_interested_btn.click()
    
        # Nom nom them cookies
        time.sleep(2)
        accept_cookies_btn = driver.find_element(By.CLASS_NAME, value="btn-primary")
        accept_cookies_btn.click()
        print("Location, Notification, and Cookie Popups dealt with.")
        
        # Time to start liking them mutts.
        time.sleep(2)
        for n in range(20):
            time.sleep(1)
            try:
                like_button = driver.find_element(By.CLASS_NAME, value='btn-like')
                like_button.click()
            except ElementClickInterceptedException:
                # Match popup is in the way — dismiss it and continue
                try:
                    driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
                except NoSuchElementException:
                    time.sleep(2)
            except NoSuchElementException:
                # Like button not loaded yet OR all dogs have been swiped — wait and retry
                time.sleep(2)                       
        likes = 20
        while likes > 0:
            try:
                like_btn = driver.find_element(By.CLASS_NAME, value="btn-like")
            except NoSuchElementException:
                time.sleep(2)
                like_btn.click()
            except ElementClickInterceptedException:
                # Handle the match popup box
                print("You've found a match.  This should be handled")
                match_btn = driver.find_element(By.CLASS_NAME, value="match-popup")
                match_btn.click()
                time.sleep(2)
            finally:
                time.sleep(2)
                like_btn.click()
        print("Pups liked")
        
    except Exception as e:
        print(f"An error has occured during execution: {e}")

    driver.quit()
    print("Browser closed")

if __name__ == "__main__":
    tindog_login()
