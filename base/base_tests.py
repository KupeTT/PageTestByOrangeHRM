import pytest

from pages.login import LoginPage
from pages.my_tracker import MyTracker
from pages.dashaboard import DashboardPage
from pages.performance import PerformancePage
from config.data import Data
from pages.my_performance_trackerlist_page import TrackListPage

class BaseTest:

    data: Data

    track_list_page = TrackListPage
    login_page = LoginPage
    dashboard_page = DashboardPage
    my_tracker = MyTracker
    performance_page = PerformancePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.my_tracker = MyTracker(driver)
        request.cls.performance_page = PerformancePage(driver)
        request.cls.track_list_page = TrackListPage(driver)
        request.cls.data = Data()

