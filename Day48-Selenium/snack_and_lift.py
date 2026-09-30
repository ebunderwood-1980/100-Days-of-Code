from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep


def run_snack_and_lift():

    # Initialize Chrome Options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    # options.add_argument("--start-maximized")    # For testing purposes only.
    options.add_argument("--disable-gpu")
    options.add_experimental_option("detach", True)

    # Initialize the webdriver
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to the website
        print("✈️Navigating to Snack and Lift Home Page")
        driver.get("https://appbrewery.github.io/gym/")
        print("✔️Website loaded successfully!")

        # Locate and click the Login Button Element
        login_button = driver.find_element(By.ID, value="login-button")
        login_button.click()
        print("🖰)Login button clicked successfully!")

        # Load up the Login Page
        print("✈️Navigating to the Login Page")
        driver.get("https://appbrewery.github.io/gym/login/")
        print("✔️Website loaded successfully!")

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
        print("✔️Login Credentials Cataloged.")

    except Exception as e:
        print(f"⚠️An error has occurred during execution: {e}")


if __name__ == "__main__":
    run_snack_and_lift()
