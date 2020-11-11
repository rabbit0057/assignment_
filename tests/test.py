import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from driver.config_driver import Driver
import HtmlTestRunner

from pages.app_install import app_install
from pages.app_launch import app_launch
from pages.app_login import app_login
from pages.app_product_search import app_product_search
from pages.app_pincode import app_pincode
from pages.app_cart import app_cart
from pages.app_addcart import app_addcart

from driver.desiredcapabilities import *

class AmazonShoppingTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver() 

    def test_TestCase_A_Amazon_App_Installed(self):
        app_install.test_1(self)

    def test_TestCase_B_Amazon_App_Launch(self):
        app_launch.test_2(self)

    def test_TestCase_C_Amazon_App_Login(self):
        app_login.test_3(self)

    def test_TestCase_D_Amazon_Adding_Pincode(self):
        app_pincode.test_4(self)
        
    def test_TestCase_E_Amazon_Search_Product(self):
        app_product_search.test_5(self)
            
    def test_TestCase_F_Amazon_Add_Product_to_Cart(self):
        app_cart.test_6(self)
        
    def test_TestCase_G_Amazon_Product_Checkout(self):
        app_addcart.test_7(self)

    def tearDown(self):
        time.sleep(2)
        self.driver.instance.quit()


if __name__ == '__main__':
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Test_Results'))
    # all the testcase results are captured in report/Test_Results as HTML file