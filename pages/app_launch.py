from locators.locators import Locators

import time

selectLanguage = ("Continue in English")

class app_launch(Locators):
    def test_1(self):
        time.sleep(2)
        self.driver.instance.implicitly_wait(5)
        self.driver.instance.find_element_by_accessibility_id(selectLanguage).click()
        self.driver.instance.implicitly_wait(5)
