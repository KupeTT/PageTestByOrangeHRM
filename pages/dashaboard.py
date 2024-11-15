from xml.sax.handler import property_encoding

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC



class DashboardPage(BasePage):


    PAGE_URL = Links.DASHBOARD_PAGE

    PERFORMANCE_BUTTON = "xpath", "//span[text()='Performance']"
    PUSH_INFO = "xpath", "//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']"

    def click_performance(self):
        self.wait.until(EC.element_to_be_clickable(self.PERFORMANCE_BUTTON)).click()

    def check_performance(self, info):
        perf_info = self.wait.until(EC.visibility_of_element_located(self.PUSH_INFO))
        assert perf_info.text == info


