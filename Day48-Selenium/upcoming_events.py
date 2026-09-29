from selenium import webdriver
from selenium.webdriver.common.by import By

# Variables and Constants
url = "https://www.python.org/"
event_dates = []
event_text = []
final_dictionary = {}


# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Initiate the driver for the Python Website
python_driver = webdriver.Chrome(options=chrome_options)
python_driver.get(url=url)


# Grab dates and corresponding text elements.
event_dates_element = python_driver.find_elements(
    By.CSS_SELECTOR, value=".event-widget time"
)
event_text_element = python_driver.find_elements(
    By.CSS_SELECTOR, value=".event-widget li a"
)


# Create two lists
event_dates = [date.text for date in event_dates_element]
event_text = [item.text for item in event_text_element]


# Create the final dictionary
final_dictionary = {
    i: {"time": k, "name": v}
    for i, (k, v) in enumerate(zip(event_dates, event_text), start=0)
}
print(final_dictionary)


# Close the Broweser
python_driver.quit()
