import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support impor expected_conditions as EC


def run_selenium_project():
    print("🚀 Starting the Selenium automation script...")

    # 1. Initialize Chrome Options (Optional configurations)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Open browser in maximized mode
    options.add_experimental_option("detach", True)

    # 2. Initialize the WebDriver
    driver = webdriver.Chrome(options=options)

    try:
        # 3. Navigate to a Website
        print("🌐 Navigating to python.org...")
        driver.get("https://python.org")

        # 4. Verify the page title (Basic assertion)
        assert "Python" in driver.title
        print("✅ Page loaded successfully! Title matches: " + driver.title)

        # 5. Locate the search bar element using its HTML ID attribute
        # <input id="id-search-field" name="q" type="search" ...>
        search_bar = driver.find_element(By.ID, "id-search-field")

        # 6. Clear any pre-existing text and type a search term
        search_bar.clear()
        print("⌨️ Typing 'documentation' into the search bar...")
        search_bar.send_keys("documentation")

        # 7. Simulate pressing the 'Enter' key to submit the search
        search_bar.send_keys(Keys.ENTER)

        # 8. Wait a brief moment for the results page to load
        time.sleep(3)

        # 9. Verify that the results page actually loaded results
        results_list = driver.find_element(By.CLASS_NAME, "list-recent-events")
        if results_list:
            print("🎉 Success! Search results were found and displayed on screen.")
        else:
            print("❌ No results container found.")

    except Exception as e:
        print(f"⚠️ An error occurred during execution: {e}")

    finally:
        # 10. Clean up and close the browser session safely
        print("🔒 Closing the browser...")
        driver.quit()


if __name__ == "__main__":
    run_selenium_project()
