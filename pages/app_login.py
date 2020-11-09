from locators.locators import *

import unittest

from driver.desiredcapabilities import *

import time

# testcase to log-in as guest  
class app_login:
    def test_3(self):
        self.driver.instance.implicitly_wait(5)
        Loginme = self.driver.instance.find_element_by_id(Locators.skipLogin)

        if Loginme.is_displayed():
            Loginme.click()
            LOGGER.info("==== Logged in as guest user")
            self.driver.instance.implicitly_wait(5)

