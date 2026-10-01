from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

booked_waitlisted = 0
waitlists_joined = 0
classes_booked = 0


def run_snack_and_lift():
    # Set up Chrome Profile
    ACCOUNT_EMAIL = "e.b.underwood@gmail.com"
    ACCOUNT_PASSWORD = "number34"
    GYM_URL = "https://appbrewery.github.io/gym/"

    # Initialize Chrome Options
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument("--start-maximized")  # For testing purposes only.
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

        # Log In as myself.
        print("✏️Logging in to  User Created Account")
        email_input = driver.find_element(By.ID, value="email-input")
        password_input = driver.find_element(By.ID, value="password-input")
        login_button = driver.find_element(By.ID, value="submit-button")
        email_input.send_keys(ACCOUNT_EMAIL)
        password_input.send_keys(ACCOUNT_PASSWORD)
        login_button.click()

        # Verify logging by checking Class Schedule page
        class_schedule_url = "https://appbrewery.github.io/gym/schedule/"
        driver.get(class_schedule_url)
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))
        print("✅Logged in. sucessfully.\n")

        # Book the Tuesday at 6pm class.
        print("👓Searching for the Tues, 7pm class")
        class_cards = driver.find_elements(
            By.CSS_SELECTOR, value="div[id^='class-card']"
        )

        # Counters for booked classes for the booking summary
        booked_count = 0
        waitlist_count = 0
        already_booked_count = 0

        for card in class_cards:
            # Get the day title from the parent day group
            day_group = card.find_element(
                By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]"
            )
            day_title = day_group.find_element(By.TAG_NAME, "h2").text

            # Check if this is a Tuesday
            if "Tue" in day_title:
                # Check if this is a 6pm class
                time_text = card.find_element(
                    By.CSS_SELECTOR, "p[id^='class-time-']"
                ).text
                if "6:00 PM" in time_text:
                    # Get the class name
                    class_name = card.find_element(
                        By.CSS_SELECTOR, "h3[id^='class-name-']"
                    ).text

                    # Find and click the book button
                    button = card.find_element(
                        By.CSS_SELECTOR, "button[id^='book-button-']"
                    )

                    # Increment the counter(s)
                    if button.text == "Booked":
                        print(f"✓ Already booked: {class_name} on {day_title}")
                        already_booked_count += 1
                    elif button.text == "Waitlisted":
                        print(f"✓ Already on waitlist: {class_name} on {day_title}")
                        already_booked_count += 1
                    elif button.text == "Book Class":
                        button.click()
                        print(f"✓ Successfully booked: {class_name} on {day_title}")
                        booked_count += 1
                        # Wait a moment for the button state to update
                        sleep(0.5)
                    elif button.text == "Join Waitlist":
                        button.click()
                        print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                        waitlist_count += 1
                        # Wait a moment for the button state to update
                        sleep(0.5)

    except Exception as e:
        print(f"⚠️An error has occurred during execution: {e}")

    # Print summary
    print("\n--- BOOKING SUMMARY ---")
    print(f"Classes booked: {booked_count}")
    print(f"Waitlists joined: {waitlist_count}")
    print(f"Already booked/waitlisted: {already_booked_count}")
    print(
        f"Total Tuesday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}"
    )


if __name__ == "__main__":
    run_snack_and_lift()
