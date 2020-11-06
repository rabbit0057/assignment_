import unittest

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

from appium.webdriver.common.touch_action import TouchAction

from appium.webdriver.common.mobileby import MobileBy

from config_driver import *
import config_driver

import HtmlTestRunner

from appium.webdriver.common.touch_action import TouchAction


selectLanguage = ("Continue in English")
skipLogin = ("in.amazon.mShop.android.shopping:id/skip_sign_in_button")
productSearch = ("in.amazon.mShop.android.shopping:id/rs_search_src_text")
pincodeLable = ("in.amazon.mShop.android.shopping:id/glow_subnav_label")
pincode = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView")
pincodeEnter = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText")
pincodeApply = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup")

tv = ("//android.view.View[@content-desc=\"Philips 164 cm (65 inches) 6700 Series 4K Ambilight LED Smart TV 65PUT6703S/94 (Dark Sliver) 3.9 out of 5 stars 11\"]/android.view.View[1]")

AddToCart =("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ViewAnimator/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[5]/android.view.View/android.view.View/android.view.View[1]/android.view.View[4]/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")

cart = ("in.amazon.mShop.android.shopping:id/chrome_action_bar_cart_count")





class AmazonShoppingTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def test_TestCase_A_Amazon_App_Launch(self):
        time.sleep(2)
        self.driver.instance.implicitly_wait(5)
        self.driver.instance.find_element_by_accessibility_id(selectLanguage).click()
        self.driver.instance.implicitly_wait(5)

    def test_TestCase_B_Amazon_App_Login(self):
        self.driver.instance.find_element_by_id(skipLogin).click()
        self.driver.instance.implicitly_wait(5)

    def test_TestCase_C_Amazon_Adding_Pincode(self):
        self.driver.instance.implicitly_wait(5)
        self.driver.instance.find_element_by_id(pincodeLable).click()
        time.sleep(2)
        self.driver.instance.implicitly_wait(5)
        self.driver.instance.find_element_by_xpath(pincode).click()
        self.driver.instance.implicitly_wait(5)
        self.driver.instance.find_element_by_xpath(pincodeEnter).click()
        self.driver.instance.find_element_by_xpath(pincodeEnter).send_keys("560095")
        time.sleep(2)
        self.driver.instance.implicitly_wait(5)
        self.driver.instance.find_element_by_xpath(pincodeApply).click()
        self.driver.instance.implicitly_wait(5)
        
    def test_TestCase_D_Amazon_Search_Product(self):
        self.driver.instance.find_element_by_id(productSearch).click()
        time.sleep(2)
        self.driver.instance.find_element_by_id(productSearch)
        self.driver.instance.find_element_by_id(productSearch).send_keys("65-inch TV")
        self.driver.instance.press_keycode(66)
        time.sleep(2)
        touch = TouchAction(self.driver.instance)
        for scrolldown in range(5):
            touch.press(x=824, y=2068).move_to(x=769, y=700).release().perform()
            
        for scrollup in range(5):
            touch.press(x=627, y=1689).move_to(x=618, y=2078).release().perform()
            
    def test_TestCase_E_Amazon_Add_Product_to_Cart(self):
        self.driver.instance.find_element_by_id(productSearch).click()
        time.sleep(2)
        self.driver.instance.find_element_by_id(productSearch)
        self.driver.instance.find_element_by_id(productSearch).send_keys("65-inch TV philips")
        self.driver.instance.press_keycode(66)
    
        self.driver.instance.find_element_by_xpath(tv).click()
        
        touch = TouchAction(self.driver.instance)
        for i in range(5):
            touch.press(x=924, y=1268)   .move_to(x=929, y=979)   .release()   .perform()
            
        time.sleep(2)
            
        self.driver.instance.find_element_by_xpath(AddToCart).click()
        
    def test_TestCase_F_Amazon_Product_Checkout(self):
        self.driver.instance.find_element_by_id(cart)

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Test_Results'))