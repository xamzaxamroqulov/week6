# Google Search Scenario:
# 1. Open the browser, launch the website google.com (Given condition in Gherkin Scenario.)
# 2. Type 'selenium python' in the search and hit Enter (Actions - When.)
# 3. Verify the result is more then 20 million.(Test here, check point - Then.)
# 4. Verify that it takes less than a second for the search.(Test here, check point - Then.)
# 5. Close the browser.
# Keywords: HTML (DOM) - Document Object Model,
# locator: xpath(querying), cssSelector(querying) can be customized using tags and attributes
# locators on html: id, name, link_name, partial_link_name, class_name.
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # Start the browser.
# or specify the path: driver = webdriver.Chrome('/path/to/chromedriver')
driver.get("https://google.com")
print("opened the browser and google website")
time.sleep(3)

search_text_box = driver.find_element_by_name("q")
print("identified google search box")
time.sleep(3)

search_text_box.clear()
search_text_box.send_keys("python selenium")
print("cleared the search box then typed 'python selenium' words in it")
time.sleep(3)
search_text_box.send_keys(Keys.RETURN)
print("hit the enter button")
time.sleep(3)

result_msg = driver.find_element_by_xpath("//div[@id='result-stats']").text
print(result_msg)
# "About 29,900,000 results (0.46 seconds)"
# verify the result num is > 20 mln
result_msg_list = result_msg.split()
result_num_str = result_msg_list[1].replace(',', '')
result_num = int(result_num_str)
assert result_num > 20000000, "Result num is less than 20 mln"
print("Verifying result number Passed.")

# Verifying the performance , less then a second.
result_time_str = result_msg_list[3].replace('(', '')
result_time = float(result_time_str)
assert result_time < 1, "Search took more than a second!"
print("Verifying search performance Passed.")

print("now closing the browser...")
driver.close()
