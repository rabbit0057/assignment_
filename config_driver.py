from appium import webdriver


class Driver:

    def __init__(self):

        desired_caps = {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "Samsung Galaxy note 10+",
            "automationName": "UiAutomator2",
            "app": "/Users/dprakash/Documents/assign_ment_Nov_/base.apk",
            "appPackage": "in.amazon.mShop.android.shopping",
            "appActivity": "com.amazon.mShop.home.HomeActivity",
            "noReset":"True"
            }

        self.instance = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
        
        
        
#        appLanguageSelection = driver.find_element_by_accessibility_id("Continue in English")
#
#        skip_sign_in_button = driver.find_element_by_id("in.amazon.mShop.android.shopping:id/skip_sign_in_button")
#
#        search_Bar_click = driver.find_element_by_id("in.amazon.mShop.android.shopping:id/rs_search_src_text")
#
#        search_Bar = driver.find_element_by_id("in.amazon.mShop.android.shopping:id/rs_search_src_text")
#
#        delivery_To = driver.find_element_by_id("in.amazon.mShop.android.shopping:id/glow_subnav_label")
#
#        pincode = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView")
#
#        pincode_Enter = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText")
#
#        pincode_Enter_Apply = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup")
#
#        tv = driver.find_element_by_xpath("//android.view.View[@content-desc='Sponsored Sanyo 139 cm (55 inches) Kaizen Series 4K Ultra HD Certified Android LED TV XT-55UHD4S (Black) (2020 Model) 4.3 out of 5 stars 473']/android.view.View[2]")













