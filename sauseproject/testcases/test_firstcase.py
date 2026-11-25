import os

import dotenv
import pytest
from sauseproject.pages import dashboard_page
from sauseproject.pages.dashboard_page import Dahboard_page
from sauseproject.pages.login_page import LoginPage
from sauseproject.utils import read_test_data
from tests.test_fristscript import test_data


# from sauseproject.utils import load_env_data


test_data = read_test_data("testdata.csv")

@pytest.mark.smoke
@pytest.mark.logintest
@pytest.mark.parametrize("row",test_data)
def test_login_test(setup,load_data,row):
        page = setup
        # page.pause()
        print("test case no",row['test case'])
        login_page = LoginPage(page)
        login_page.launch_url()
        login_page.enter_username(row['username'])
        login_page.enter_password(row['password'])
        # login_page.click_login()
        dashboard_page=Dahboard_page(page)
        dashboard_page.assert_title(os.environ['title'])
        dashboard_page.logout()
        print("test login_test is completed")

@pytest.mark.checkout
# @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce",)])
def test_login_checkout(load_data,setup):
    page = setup
    login_page = LoginPage(page)
    login_page.launch_url()
    login_page.enter_username(os.environ['test_username'])
    login_page.enter_password(os.environ['password'])
    login_page.click_login()
    dashboard_page = Dahboard_page(page)
    dashboard_page.add_product()
    dashboard_page.click_checkout()
    assert dashboard_page.verify_product_added()
    dashboard_page.logout()
    print("test checkout_test is completed")
