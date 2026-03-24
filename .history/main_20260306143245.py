import pytest
from selenium import webdriver

# Replace 'webdriver.Chrome()' with the appropriate driver if using a different browser
driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)  # Should print the title of the webpage
driver.quit()