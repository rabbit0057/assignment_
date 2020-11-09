from driver.desiredcapabilities import *

# test case to check if the app is installed sucessfully
class app_install:
    def test_1(self):
        self.driver.instance.is_app_installed(TestappPackage)
        LOGGER.info("==== APP Installed sucessfully and verified")