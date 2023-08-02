from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import  By
from ConfigTest.read_global_data import Testdata
from Pages.BasePages import Base


class Homepage(Base):

         #element identificaion related to homepage
         Menubar =(By.XPATH, "//button[@id='react-burger-menu-btn']")
         LogOutLink = (By.CSS_SELECTOR, "body > div.page-wrapper > header > div.panel.wrapper > div > ul > li.customer-welcome.active > div > ul > li.authorization-link > a")
         Logo = (By.XPATH,"//a[@class='logo']")
         CustomerName = (By.CSS_SELECTOR, 'body > div.page-wrapper > header > div.panel.wrapper > div > ul > li.customer-welcome > span > button')
         UserLogined = (By.XPATH,"//span[@class='logged-in']")
         # MyOrderClick = (By.CSS_SELECTOR, "#block-collapsible-nav > ul > li.nav.item.current > strong")
         MyOrderClick = (By.CSS_SELECTOR,"#block-collapsible-nav > ul > li:nth-child(2) > a")
         Search = (By.XPATH, "//input[@id='search']")
         Searchsubmit = (By.XPATH,"//button[@type='submit' and @title='Search']")
         Menu1 = (By.XPATH, "//*[@id='ui-id-7']")
         Img = (By.XPATH,"//input[@id='newsletter']")
         Img_1 = (By.CSS_SELECTOR, "#maincontent > div.columns > div.column.main > div.search.results > div.products.wrapper.grid.products-grid > ol > li:nth-child(1) > div > a > span > span > img")
         Itemsize = (By.XPATH,"//*[@id='option-label-size-143-item-167']")
         Itemcolor = (By.XPATH,"//*[@id='option-label-color-93-item-50']")
         Addtocart = (By.XPATH,"//button[@id='product-addtocart-button']")
         cartCount = (By.XPATH, "//span[@class='counter-number']")
         deleteItem = (By.XPATH, "//a[@title ='Remove item']")
         Okaccept = (By.XPATH, "//button[@class='action-primary action-accept']")


         def __init__(self, driver):
             super().__init__(driver)
             self.driver.get(Testdata.row_data[2])

         def do_check_logo(self):
             return self.check_is_displayed(self.Logo)

         def do_click_menu(self):
             self.do_click(self.CustomerName)

         def do_click_main_menu(self):
             self.do_click(self.Menu1)

         def do_logout_check(self):
             self.do_click(self.LogOutLink)

         def do_Click_Myorders(self):
             self.do_click(self.MyOrderClick)

         def get_userLogined_text(self):
             self.do_get_element_text(self.UserLogined)

         def do_search_item(self,text):
             self.do_sendkeys(self.Search,text)

         def do_search_submit(self):
             self.do_click(self.Searchsubmit)

         def do_find_scroll(self):
             self.do_scroll_to_element(self.Img_1)
             self.do_click(self.Img_1)

         def do_scroll_height(self):
             self.do_scroll_by_height(self.Itemsize)

         def do_wait(self):
             self.wait_page_load()

         def do_click_itemsize(self):
             self.do_click(self.Itemsize)

         def do_click_itemcolor(self):
             self.do_click(self.Itemcolor)

         def do_click_add_to_cart(self):
             self.do_click(self.Addtocart)

         def do_get_cart_count(self):
             self.do_click(self.cartCount)

         def do_click_delete_item(self):
             self.do_click(self.deleteItem)

         def do_click_delete_accept(self):
             self.do_click(self.Okaccept)








