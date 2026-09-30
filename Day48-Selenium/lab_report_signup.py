from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Variables
url = "https://appbrewery.github.io/fake-newsletter-signup/"
search_btn = None
first_box = None
last_box = None
email_box = None
FIRST = "Eric"
LAST = "Underwood"
EMAIL = "e.b.underwood@gmail.com"

# Set up Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Initiate webdriver
form_driver = webdriver.Chrome(options=chrome_options)
form_driver.get(url=url)


# Grab the button element to be pushed
search_btn = form_driver.find_element(By.CSS_SELECTOR, value="form button")


# Grab the first, last, and email text box elements
first_box = form_driver.find_element(By.NAME, value="fName")
last_box = form_driver.find_element(By.NAME, value="lName")
email_box = form_driver.find_element(By.NAME, value="email")


# Fill out the boxes
first_box.send_keys(FIRST)
last_box.send_keys(LAST)
email_box.send_keys(EMAIL)


# Click the Sign Up Box
search_btn.click()


# Close the window
# form_driver.quit()
