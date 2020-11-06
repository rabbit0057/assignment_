from appium import webdriver

import os


class Driver:

    def __init__(self):

        desired_caps = {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "Samsung Galaxy note 10+",
            "deviceName": "Samsung Galaxy note 10+",
            "automationName": "UiAutomator2",
            "app": os.path.abspath(os.path.join(os.path.dirname(__file__),"Amazon_shopping.apk")),
            "appPackage": "in.amazon.mShop.android.shopping",
            "appActivity": "com.amazon.mShop.home.HomeActivity",
            "noReset":"True"
            }


        self.instance = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
        
        
        














