from locators.locators import Locators

import time
from appium.webdriver.common.touch_action import TouchAction

productSearch = ("in.amazon.mShop.android.shopping:id/rs_search_src_text")
AddToCart =("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ViewAnimator/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[5]/android.view.View/android.view.View/android.view.View[1]/android.view.View[4]/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
cart = ("in.amazon.mShop.android.shopping:id/chrome_action_bar_cart_count")

tv = ("//android.view.View[@content-desc=\"Philips 164 cm (65 inches) 6700 Series 4K Ambilight LED Smart TV 65PUT6703S/94 (Dark Sliver) 3.9 out of 5 stars 11\"]/android.view.View[1]")


class app_cart:
    # def __init__(self, driver):
    #     self.driver = driver
        # self.selectLanguage = Locators.selectLanguage

    def test_5(self):
        self.driver.instance.find_element_by_id(productSearch).click()
        time.sleep(2)
        
        try:
            self.driver.instance.find_element_by_id(productSearch)
            self.driver.instance.find_element_by_id(productSearch).send_keys("65-inch TV philips")
            self.driver.instance.press_keycode(66)
            assert productSearch == "65-inch TV philips"
        
        finally:


            self.driver.instance.implicitly_wait(5)
            self.driver.instance.find_element_by_xpath(tv).click()

            touch = TouchAction(self.driver.instance)
            for i in range(2):
                touch.press(x=636, y=2101).move_to(x=627, y=499).release().perform()
    
        
            self.driver.instance.implicitly_wait(5)
            self.driver.instance.find_element_by_xpath(AddToCart).click()