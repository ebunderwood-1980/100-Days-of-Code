from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")
driver.maximize_window()

# Wait for page to load just in case
time.sleep(3)

# Handle initial popups (cookies consent does not have to be clicked, but language does)
print("Looking for language selection...")
try:
    # Select English language
    print("Selecting language")
    language_button = driver.find_element(by=By.CSS_SELECTOR, value="#langSelect-EN")
    language_button.click()
    print("...Done")
except Exception as e:
    print(f"Exception: {e}")

print("Finding the cookie")
driver.get(url="https://ozh.github.io/cookieclicker/")
cookie = driver.find_element(By.ID, value="bigCookie")


# Set time for upgrade interval
upgrade_interval = 5
upgrade_time = time.time() + upgrade_interval

# Set time to stop program execution
stop_time = time.time() + 60

while True:
    cookie.click()

    if time.time() >= upgrade_time:
        # Get all enabled products
        products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

        # If enabled products exists, click on all enabled product starting from the last item (most expensive).
        # Technically, more expensive item can appear earlier in the list but
        #   that's unlikely based on the bot executes its logic.
        if products:
            products[len(products) - 1].click()
            # for product in reversed(products):
            #     if "enabled" in product.get_attribute("class"):
            #         product.click()

        # Reset upgrade interval
        upgrade_time = time.time() + upgrade_interval

    # Stop program execution
    if time.time() >= stop_time:
        break

print(driver.find_element(By.XPATH, value="//*[@id='cookies']/div").text)

driver.quit()
