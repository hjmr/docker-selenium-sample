import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options)
print("remote")
driver.get("https://www.google.com/")
time.sleep(5)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys('M3 Mac')
search_box.submit()
time.sleep(5)
driver.save_screenshot("google_search_screenshot.png")
results = driver.find_elements(By.XPATH, '//div[@class="g"]/*/*/*/*/*/*/h3')
for element in results:
    print(element.tag_name, element.get_attribute('innerHTML'))
driver.quit()
