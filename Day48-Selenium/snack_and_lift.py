from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

def run_snack_and_lift():
    # Set up Chrome Profile
    ACCOUNT_EMAIL = "e.b.underwood@gmail.com"
    ACCOUNT_PASSWORD  = "number34"
    GYM_URL = "https://appbrewery.github.io/gym/"
    
    # Initialize Chrome Options
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument("--start-maximized")    # For testing purposes only.
    options.add_argument("--disable-gpu")
    options.add_experimental_option("detach", True)
    user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # Initialize the webdriver
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to the website
        print("✈️Navigating to Snack and Lift Home Page")
        driver.get("https://appbrewery.github.io/gym/")
        print("✔️Website loaded successfully!\n")

        # Locate and click the Login Button Element
        login_button = driver.find_element(By.ID, value="login-button")
        login_button.click()
        print("🖰)Login button clicked successfully!\n")

        # Load up the Login Page
        print("✈️Navigating to the Login Page")
        driver.get("https://appbrewery.github.io/gym/login/")
        print("✔️Website loaded successfully!\n")

        # Get Admin Username and Password
        print("📓Accessing Login Credentials")
        login_credentials_element = driver.find_elements(
            By.CLASS_NAME, value="Login_credentialDetail__Mu9oI"
        )
        login_credentials = [(item.text).strip() for item in login_credentials_element]
        credential_dict = {
            "student": {
                "username": login_credentials[0].split(":")[1].strip(),
                "password": login_credentials[1].split(":")[1].strip(),
            },
            "admin": {
                "username": login_credentials[2].split(":")[1].strip(),
                "password": login_credentials[3].split(":")[1].strip(),
            },
        }
        print("✔️Login Credentials Cataloged.\n")

        # Log In as Admin
        print("✏️Logging in to  User Created Account")
        email_input = driver.find_element(By.ID, value="email-input")
        password_input = driver.find_element(By.ID, value="password-input")
        login_button = driver.find_element(By.ID, value="submit-button")
        email_input.send_keys(ACCOUNT_EMAIL)
        password_input.send_keys(ACCOUNT_PASSWORD)
        login_button.click()
        print("✅Logged in. sucessfully.")
        
    except Exception as e:
        print(f"⚠️An error has occurred during execution: {e}")


if __name__ == "__main__":
    run_snack_and_lift()
