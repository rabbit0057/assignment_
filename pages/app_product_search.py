from locators.locators import *

from appium.webdriver.common.touch_action import TouchAction

from driver.desiredcapabilities import *


import time

# testcase to find the product in the search bar
class app_product_search:
    def test_5(self):
        LOGGER.info("==== Search Bar ")
        productsearch = self.driver.instance.find_element_by_id(Locators.productSearch)
        productsearch.click()
        time.sleep(2)

        try:
            self.driver.instance.find_element_by_id(Locators.productSearch)
            LOGGER.info("==== Searching for product ")
            productsearch.send_keys("65-inch TV")
            assert Locators.productSearch == Locators.pincodeApply
        finally:
            
            self.driver.instance.press_keycode(66)
            time.sleep(2)

            # performing touch function of scrolling down and up
            LOGGER.info("==== Performing scroll function ")
            touch = TouchAction(self.driver.instance)
            for scrolldown in range(5):
                touch.press(x=824, y=2068).move_to(x=769, y=700).release().perform()
            
            for scrollup in range(5):
                touch.press(x=627, y=1689).move_to(x=618, y=2078).release().perform()