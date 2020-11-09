from locators.locators import Locators

import time

cart = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout")

cartcount = ("in.amazon.mShop.android.shopping:id/chrome_action_bar_cart_count")

class app_addcart:
    def test_6(self):
        self.driver.instance.find_element_by_xpath(cart)
