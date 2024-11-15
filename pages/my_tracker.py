from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class MyTracker(BasePage):

    PAGE_URL = Links.MY_TRACKERS_PAGE

    BUTTON_VIEW = "xpath", "//button[@name='view']"

    def click_view(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_VIEW)).click()