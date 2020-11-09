from locators.locators import Locators

import time

skipLogin = ("in.amazon.mShop.android.shopping:id/skip_sign_in_button")


class app_login:
    def test_2(self):
        self.driver.instance.find_element_by_id(skipLogin).click()
        self.driver.instance.implicitly_wait(5)