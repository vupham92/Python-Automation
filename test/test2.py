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
        assert len(num_slider) == 3

    def test_homepage02(self,test_setup):
        driver.get("http://practice.automationtesting.in/")
        driver.find_element_by_id("menu-item-40").click()
        driver.find_element_by_id("site-logo").click()
        num_arrivals = driver.find_elements_by_id("text-22-sub_row_1-0-2-")
        assert len(num_arrivals) == 3

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("TEST COMPLETED")
