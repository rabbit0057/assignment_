from locators.locators import Locators

import time

pincodeLable = ("in.amazon.mShop.android.shopping:id/glow_subnav_label")
pincode = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView")
pincodeEnter = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText")
pincodeApply = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup")



class app_pincode(Locators):
    def test_3(self):
        self.driver.instance.implicitly_wait(5)
        self.driver.instance.find_element_by_id(pincodeLable).click()
        time.sleep(2)
        self.driver.instance.implicitly_wait(5)
        self.driver.instance.find_element_by_xpath(pincode).click()
        self.driver.instance.implicitly_wait(5)

        try:
            self.driver.instance.find_element_by_xpath(pincodeEnter).click()
            self.driver.instance.find_element_by_xpath(pincodeEnter).send_keys("560095")
            assert pincodeEnter == "560095"
        finally:

            time.sleep(2)
            self.driver.instance.implicitly_wait(5)
            self.driver.instance.find_element_by_xpath(pincodeApply).click()
            self.driver.instance.implicitly_wait(5)