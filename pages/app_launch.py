from locators.locators import *

from driver.desiredcapabilities import *

import unittest
from selenium.common.exceptions import NoSuchElementException


import time

# testcase to launch and select english as language 
class app_launch:
    def test_2(self):
        self.driver.instance.back()
        time.sleep(2)   
        self.driver.instance.implicitly_wait(5)
        appLanguageSelection = self.driver.instance.find_element_by_accessibility_id(Locators.selectLanguage)

        if appLanguageSelection.is_displayed():
            LOGGER.info("==== English language button is displayed")
            appLanguageSelection.click()
            LOGGER.info("==== Selected english as language")
            self.driver.instance.implicitly_wait(5)

      

        


