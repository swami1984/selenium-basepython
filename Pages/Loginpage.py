from webdriver_manager.chrome import ChromeDriverManager
from ConfigTest.read_global_data import Testdata
from Pages.BasePages import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import service, Service
from Pages.BasePages import Base
from selenium.webdriver.common.by import By
from Pages.Homepage import Homepage

class Loginpage(Base):

    EMAIL = (By.XPATH, "//input[@id='email']")
    PASS = (By.XPATH, "//input[@id='pass']")
    LOGIN_BTN = (By.XPATH, "//button[@id='send2']")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logoutLink']")


    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(Testdata.row_data[2])

    def do_login_signup(self,username, password):
        self.do_sendkeys(self.EMAIL,username)
        self.do_sendkeys(self.PASS,password)
        self.do_click(self.LOGIN_BTN)
        return Homepage(self.driver)











