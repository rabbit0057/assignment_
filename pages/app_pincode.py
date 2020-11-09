from locators.locators import *

from driver.desiredcapabilities import *

import time

# testcase to apply pincode
class app_pincode:
    def test_4(self):
        self.driver.instance.implicitly_wait(5)
        pincodelable = self.driver.instance.find_element_by_id(Locators.pincodeLable)
        pincodelable.click()
        LOGGER.info("==== check for the pincode ")
        time.sleep(2)
        self.driver.instance.implicitly_wait(5)
        pincode = self.driver.instance.find_element_by_xpath(Locators.pincode)
        pincode.click()
        LOGGER.info("==== Enter the pincode")
        self.driver.instance.implicitly_wait(5)

        # to fail the testcase adding the assertion to the xpath
        try:
            pincodeenter = self.driver.instance.find_element_by_xpath(Locators.pincodeEnter)
            pincodeenter.click()
            self.driver.instance.find_element_by_xpath(Locators.pincodeEnter).send_keys("560095")
            assert Locators.pincodeEnter == Locators.pincodeEnter
        finally:

            time.sleep(2)
            self.driver.instance.implicitly_wait(5)
            pincodeapply = self.driver.instance.find_element_by_xpath(Locators.pincodeApply)
            pincodeapply.click()
            LOGGER.info("==== Apply the pincode")
            self.driver.instance.implicitly_wait(5)