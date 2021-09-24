from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

#Test open Chrome brower
#def test():
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://practice.automationtesting.in/")
print(driver.title)
page_title = driver.title
assert 'Automation Practice Site' in page_title
driver.quit()

