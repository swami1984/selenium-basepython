from selenium import webdriver
from  selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from Test.test_base import BaseClass


class Base():

    def __init__(self,driver):
        self.driver = driver

    def do_click(self,by_locator):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(by_locator)).click()

    def do_sendkeys(self,by_locator,text):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_logout(self,by_locator):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(by_locator)).click()

    def do_get_element_text(self,by_locator):
        element = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def check_is_displayed(self,by_locator):
        element = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def do_move_to_element(self,by_locator):
        # element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        element =  WebDriverWait(self.driver,30).until(EC.presence_of_element_located(by_locator))
        ele = ActionChains(self.driver)
        ele.move_to_element(by_locator).perform()
        ele.scroll_to_element(element)

    def do_scroll_to_element(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script('arguments[0].scrollIntoView(true)',element)
        self.driver.execute_script('scrollBy(0,1000)''')
        # ele = ActionChains(self.driver)
        # ele.scroll_to_element(element)

    def do_scroll_by_height(self,by_locator):
         element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
         self.driver.execute_script('arguments[0].scrollIntoView(true)', element)

    def wait_page_load(self):
        self.driver.implicitly_wait(3000)













