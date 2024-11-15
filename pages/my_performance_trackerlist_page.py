
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class TrackListPage(BasePage):

    PAGE_URL = Links.TRACKER_LOG

    BUTTON_ADD_LOG = "xpath", "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    INPUT_LOG = "xpath", "(//input[@class='oxd-input oxd-input--active'])[2]"
    INPUT_COMMENT = "xpath", "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']"
    BUTTON_NEGATIV = "xpath", "//button[@class='oxd-button oxd-button--medium oxd-button--text orangehrm-tracker-rating-button']"
    BUTTON_SAVE = "xpath", "//button[@type='submit']"


    def click_add_log(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_ADD_LOG)).click()

    def input_log(self, log):
        self.wait.until(EC.element_to_be_clickable(self.INPUT_LOG)).send_keys(log)

    def input_comment(self, comment):
        self.wait.until(EC.element_to_be_clickable(self.INPUT_COMMENT)).send_keys(comment)

    def click_negativ(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_NEGATIV)).click()

    def save_comment(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SAVE)).click()

    def execut_save_comment(self):
        save_button = self.wait.until(
            EC.presence_of_element_located(self.BUTTON_SAVE)
        )
        self.driver.execute_script("arguments[0].click();", save_button)