from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Loginpage import Loginpage
from  ConfigTest.read_global_data import Testdata
from Test.test_base import BaseClass


class Test_Login_Page(BaseClass):

    def test_do_login(self):
       self.loginpage =  Loginpage(self.driver)
       # self.loginpage.do_login_signup(Testdata.USER_NAME,Testdata.PASS_WORD)
       self.loginpage.do_login_signup(Testdata.row_data[0],Testdata.row_data[1])
