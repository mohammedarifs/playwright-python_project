


import pytest
from playwright.sync_api import sync_playwright, Page, expect  # fixture

from sauseproject.pages import dashboard_page
from sauseproject.pages.dashboard_page import Dahboard_page
from sauseproject.pages.login_page import LoginPage


@pytest.fixture
# @pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
def setup():
        with sync_playwright() as playwright:
                browser = getattr(playwright, "chromium").launch(headless=False)
                context=browser.new_context()
                page = context.new_page()
                yield page
                browser.close()

@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize("username,password",[("standard_user","secret_sauce",)])
def test_login_test(setup,username,password):
        page = setup
        # page.pause()
        login_page = LoginPage(page)
        login_page.launch_url()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        dashboard_page=Dahboard_page(page)
        dashboard_page.assert_title("Swag Labs")
        dashboard_page.logout()
        print("test login_test is completed")

@pytest.mark.checkout
@pytest.mark.parametrize("username,password",[("standard_user","secret_sauce",)])
def test_login_checkout(setup, username, password):
    page = setup
    login_page = LoginPage(page)
    login_page.launch_url()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    dashboard_page = Dahboard_page(page)
    dashboard_page.add_product()
    dashboard_page.click_checkout()
    assert dashboard_page.verify_product_added()
    dashboard_page.logout()
    print("test checkout_test is completed")
