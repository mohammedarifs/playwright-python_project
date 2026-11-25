import os

import pytest
from sauseproject.pages.dashboard_page import Dahboard_page
from sauseproject.pages.login_page import LoginPage
from sauseproject.utils import read_test_data

test_data = read_test_data("testdata.csv")

@pytest.mark.parametrize("row", test_data)
@pytest.mark.secondtestcase
def test_login_second_case(setup,load_data,row):
    page = setup
    # page.pause()
    login_page = LoginPage(page)
    login_page.launch_url()
    login_page.enter_username(row["username"])
    login_page.enter_password(row["password"])
    login_page.click_login()
    dashboard_page = Dahboard_page(page)
    # print(os.environ['title'])
    dashboard_page.assert_title(os.environ['title'])
    assert page.title() == "Swag Labs", "not able to login"
    dashboard_page.logout()
    print("test login_test is completed")
    page.close()
