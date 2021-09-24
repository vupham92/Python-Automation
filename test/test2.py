from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class TestHomePage():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("TEST COMPLETED")

    def test_homepage01(self,test_setup):
        driver.get("http://practice.automationtesting.in/")
        print(driver.title)
        driver.find_element_by_id("menu-item-40").click()
        driver.find_element_by_id("site-logo").click()
        num_slider = driver.find_elements_by_class_name("n2-ss-slide")
        if len(num_slider) == 3:
            print("Home Page contains only three sliders")
        else:
            print("Home page does note contain three sliders")

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("TEST COMPLETED")
