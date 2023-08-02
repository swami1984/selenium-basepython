from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import service,Service


@pytest.fixture(params=["Chrome"],scope='class')
def init_driver(request):
    if request.param == "Chrome":
        chr_option =Options()
        chr_option.add_experimental_option("detach",True)
        web_chrome =webdriver.Chrome(options = chr_option,service= Service(ChromeDriverManager(driver_version="114.0.5735.90").install()))
        request.cls.driver = web_chrome
        web_chrome.delete_all_cookies()
        web_chrome.maximize_window()
        web_chrome.implicitly_wait(60)
    yield
    web_chrome.quit()










