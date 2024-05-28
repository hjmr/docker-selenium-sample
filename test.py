import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME)
print("remote")
driver.get("https://www.google.com/")
time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys('M3 Mac')
search_box.submit()
time.sleep(5)
driver.save_screenshot("google_search_screenshot.png")
results = driver.find_elements_by_xpath("//div[@id='search']/*/*/div[@class='g']/div/div/div/a")
for element in results:
    print(element.text)
driver.quit()
