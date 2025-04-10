from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles=driver.find_element(By.XPATH,value='//*[@id="articlecount"]/a[1]')
# articles.click()
#
# print(articles.text)

# portals=driver.find_element(By.LINK_TEXT,value="The Summer Paralympics")
# portals.click()

search=driver.find_element(By.NAME,value="search")
#sending keyboard inputs to selenium
search.send_keys("Python",Keys.ENTER)


# driver.quit()