from locators.locators import *
import time
from appium.webdriver.common.touch_action import TouchAction

from driver.desiredcapabilities import *


# testcase to find the TV in search bar and add it the cart
class app_cart:
    def test_6(self):
        productsearch = self.driver.instance.find_element_by_id(Locators.productSearch)
        productsearch.click()
        LOGGER.info("==== Search Bar ")
        time.sleep(2)
        
        try:
            self.driver.instance.find_element_by_id(Locators.productSearch)
            productsearch.send_keys("65-inch TV philips")
            LOGGER.info("==== Searching for product ")
            self.driver.instance.press_keycode(66)
            self.driver.instance.implicitly_wait(5)
            LOGGER.info("==== Searching for 65-inch TV")
            tvs = self.driver.instance.find_element_by_xpath(Locators.tv)
            tvs.click()
            assert Locators.tv == Locators.tv
        finally:

            # performing touch function of scrolling down to click on add to cart button
            touch = TouchAction(self.driver.instance)
            for i in range(2):
                touch.press(x=636, y=2101).move_to(x=627, y=499).release().perform()
    
            # self.driver.instance.implicitly_wait(5)
            time.sleep(10)
            add = self.driver.instance.find_element_by_xpath(Locators.AddToCart)
            if add.is_displayed():
                add.click()
                LOGGER.info("==== Performing scroll to find addtocart button ")
            else:
                LOGGER.info("==== add to cart button not found in the screen ")
            
