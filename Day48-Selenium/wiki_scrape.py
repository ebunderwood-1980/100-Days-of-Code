from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Variables and Contstants
url = "https://en.wikipedia.org/wiki/Main_Page"
ebay_url = "https://ebay.com"
article_count = None


# Set up Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Initate the Wikipedia Selenium Driver
wiki_driver = webdriver.Chrome(options=chrome_options)
wiki_driver.get(url=url)


# Grab active editors element
article_count = wiki_driver.find_element(By.ID, value="mwDw")
print(article_count.text)


# Click on the active editors link
# article_count.click()
billboard_link = wiki_driver.find_element(By.LINK_TEXT, value="Billboard Hot 100")
# billboard_link.click()
wiki_driver.quit()

ebay_driver = webdriver.Chrome(options=chrome_options)
ebay_driver.get(url=ebay_url)

search_link = ebay_driver.find_element(By.NAME, value="_nkw")
search_link.send_keys("Moonlander Keyboard", Keys.ENTER)
# Close the browser
# wiki_driver.quit()
