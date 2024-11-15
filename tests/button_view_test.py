import time

from base.base_tests import BaseTest

class TestButton(BaseTest):

    # def test_click_button_view(self):
    #     self.login_page.open()
    #     self.login_page.is_open()
    #     self.login_page.enter_login(self.data.LOGIN)
    #     self.login_page.enter_password(self.data.PASSWORD)
    #     self.login_page.click_login()
    #     self.dashboard_page.is_open()
    #     self.dashboard_page.click_performance()
    #     self.dashboard_page.check_performance("Info")
    #     self.performance_page.is_open()
    #     self.performance_page.click_my_tracker()
    #     self.my_tracker.is_open()
    #     self.my_tracker.click_view()

    def test_add_comment(self):
        self.login_page.open()
        self.login_page.is_open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login()
        self.track_list_page.open()
        self.track_list_page.is_open()
        self.track_list_page.click_add_log()
        self.track_list_page.input_log("No good")
        self.track_list_page.input_comment("Very not good comment")
        self.track_list_page.click_negativ() # Кнопка не нажимается
        self.track_list_page.execut_save_comment() #Временная затычка
