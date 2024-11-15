from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class PerformancePage(BasePage):

    PAGE_URL = Links.PERFORMANCE_PAGE

    MY_TRACKER = "xpath", "//a[text()='My Trackers']"

    def click_my_tracker(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_TRACKER)).click()