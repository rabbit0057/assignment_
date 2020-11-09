from locators.locators import Locators

from appium.webdriver.common.touch_action import TouchAction


import time


productSearch = ("in.amazon.mShop.android.shopping:id/rs_search_src_text")


class app_product_search:
    def test_4(self):
        self.driver.instance.find_element_by_id(productSearch).click()
        time.sleep(2)

        try:
            self.driver.instance.find_element_by_id(productSearch)
            self.driver.instance.find_element_by_id(productSearch).send_keys("65-inch TV")
            assert productSearch == "65-inch TV"
        finally:

            self.driver.instance.press_keycode(66)
            time.sleep(2)
            touch = TouchAction(self.driver.instance)
            for scrolldown in range(5):
                touch.press(x=824, y=2068).move_to(x=769, y=700).release().perform()
            
            for scrollup in range(5):
                touch.press(x=627, y=1689).move_to(x=618, y=2078).release().perform()