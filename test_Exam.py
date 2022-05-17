from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from x_path import X_path


def find_element(text_from_amazon):
    i = "iPhone"
    if i in text_from_amazon:
        return i


driver = webdriver.Chrome()


class TestIPhon:
    @pytest.fixture()
    def test_amazon(self):
        global driver
        driver = webdriver.Chrome()
        driver.get(X_path.amazon)
        driver.implicitly_wait(2)
        driver.maximize_window()
        search_input = driver.find_element(By.XPATH, X_path.input_search_text)
        search_input.send_keys('iPhone')
        search_click = driver.find_element(By.XPATH, X_path.click_search)
        search_click.click()
        yield
        driver.close()
        driver.quit()

    def test_first(self, test_amazon):
        element1 = driver.find_element(By.XPATH, X_path.element1_text).text
        check_word = find_element(element1)
        assert check_word == "iPhone"

    def test_second(self, test_amazon):
        element2 = driver.find_element(By.XPATH, X_path.element2_text).text
        check_word = find_element(element2)
        assert check_word == "iPhone"

    def test_third(self, test_amazon):
        element3 = driver.find_element(By.XPATH, X_path.element3_text).text
        check_word = find_element(element3)
        assert check_word == "iPhone"
