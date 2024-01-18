import webbrowser
from ssl import Options

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(
#     By.XPATH,
#     "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]",
# )
#
# article_count.click()
# print(article_count.text)

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search <input> by Name
search = driver.find_element(By.NAME, value="search")
# Sending keyboard input to Selenium
search.send_keys("Python")

# driver.quit()
