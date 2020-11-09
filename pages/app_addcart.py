from locators.locators import *

import time

from driver.desiredcapabilities import *

#testcase to check the product is the cart
class app_addcart:
    def test_7(self):
        self.driver.instance.implicitly_wait(5)
        checkcart = self.driver.instance.find_element_by_xpath(Locators.cart)
        checkcart.click()
        LOGGER.info("==== Checking the cart ")
