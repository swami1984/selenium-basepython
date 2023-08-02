from selenium import webdriver
from selenium.webdriver.common.by import  By
from webdriver_manager.chrome import ChromeDriverManager
from ConfigTest.read_global_data import Testdata
from Pages.Loginpage import Loginpage
from Pages.Homepage import Homepage
from Test.test_base import BaseClass


class Test_HomePage(BaseClass):

    def test_login(self):
        self.home = Loginpage(self.driver)
        # self.home.do_login_signup(Testdata.user_name,Testdata.pass_word)
        self.home.do_login_signup(Testdata.row_data[0], Testdata.row_data[1])

    def test_verify_logo(self):
       self.home = Homepage(self.driver)
       element =self.home.do_check_logo()
       return bool(element)

    def test_check_myorders(self):
        self.home = Homepage(self.driver)
        self.home.do_Click_Myorders()

    def test_search_submit(self):
        self.home = Homepage(self.driver)
        self.home.do_search_item(Testdata.row_data[3])
        self.home.do_search_submit()
        self.home.do_wait()
        self.home.do_find_scroll()
        self.home.do_wait()
        self.home.do_scroll_height()
        self.home.do_wait()
        self.home.do_click_itemsize()
        self.home.do_wait()
        self.home.do_click_itemcolor()
        self.home.do_wait()
        self.home.do_click_add_to_cart()
        self.home.do_wait()
        # expected = self.home.do_get_cart_count()
        # assert expected == Testdata.cart


    # def test_loginuser_check(self):
    #     self.home = Homepage(self.driver)
    #     usertext = self.home.get_userLogined_text()
    #     assert usertext == Testdata.User

    def test_click_main_menu(self):
        self.home = Homepage(self.driver)
        self.home.do_click_main_menu()

    def test_click_cart(self):
        self.home = Homepage(self.driver)
        self.home.do_get_cart_count()
        self.home.do_click_delete_item()
        self.home.do_click_delete_accept()

    def test_click_menu(self):
        self.home = Homepage(self.driver)
        self.home.do_click_menu()
        self.home.do_logout_check()

    # def test_logout(self):
    #     self.home = Homepage(self.driver)
    #     self.home.do_logout_check



