from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = "https://www.amazon.com/Oakley-Non-Polarized-Rectangular-Sunglasses-Polished/dp/B079N9G2N7/ref=sr_1_24?crid=35N4U6HAVAKX3&dib=eyJ2IjoiMSJ9.Xg6QE7O7BS5IUGjbYDunquz_e00751UYD9fgFsvr43inat6KS2Z4TlO7L1xxWMc5Idbcl2W3UMlVLbR-kLiEUR93mJ99WRAd0CdDsix4c1pAdZ4ROf98hzBR6QJV0Ub22bFW8la6RPvjwiayhg16bwFmjOl-wGMnS2rgZ38KPPfG7esY3aqMu-4ruUM8s_Qon_2NiHeTOCkA-6lDcl0bS1Jr-lfAPXlwA-HNudf1yoavIAKktNMwePCfrxQzSrnThIO6DjGBabNxoYnNp18W09FjN585PkI4bLGrO1xQ6BU.BFNR3szTvFhfxTDfWDKdDmXqB_p-Eog6HjCPt-EytAk&dib_tag=se&keywords=oakley%2Bsunglasses%2Bfor%2Bmen&qid=1790657922&sprefix=oak%2Caps%2C166&sr=8-24&th=1"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome browser driver once to stop from being flagged as a bot.
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")
time.sleep(2)

# Actually get the product website.
driver.get(url=url)

# Scrape the price of the item.
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

# Print out the price
print(f"${price_dollar}.{price_cent}")

# Close the browser window
driver.quit()
