import time
from idlelib import browser

import pytest
from playwright.sync_api import sync_playwright,Page#fixture



@pytest.fixture
# @pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
def setup():
        with sync_playwright() as playwright:
                # if browser_name == "chromium":
                #         browser = playwright.chromium.launch(headless=False)
                # elif browser_name == "firefox":
                #         browser = playwright.firefox.launch(headless=False)
                # elif browser_name == "webkit":
                #         browser = playwright.webkit.launch(headless=False)
                # else:
                #         raise ValueError(f"Unsupported browser: {browser_name}")
                browser = getattr(playwright, "chromium").launch(headless=False)
                context=browser.new_context()
                page = context.new_page()
                yield page,context
                browser.close()

@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize("username,password",[("standard_user","secret_sauce",),("locked_out_user","secret_sauce")])
def test_login_test(setup,username,password):
        page = setup
        # page.pause()
        page.goto("https://www.saucedemo.com/")
        print("get the cred", username,password)
        print("get the title of applcaiotion ",page.title())
        page.locator("[name='user-name']").fill(username)
        page.get_by_placeholder("Password").fill(password)
        page.get_by_role("button", name="Login").click()
        assert page.title() == "Swag Labs","not able to login"
        page.get_by_text("Open Menu").click()
        page.get_by_text("Logout").click()
        print("test login_test is completed")
        page.close()

@pytest.mark.smoke
@pytest.mark.addtocart
def test_addto_cart(page: Page):
        # page.pause()
        page.goto("https://www.saucedemo.com/")
        print("get the title of applcaiotion ",page.title())
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()
        page.close()

@pytest.mark.orderplace
def test_order_place(page: Page):
        # page.pause()
        page.goto("https://www.saucedemo.com/")
        print("get the title of applcaiotion ",page.title())
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()
        page.close()




def test_actionsinplaywright(setup):
        page,context = setup
        # page.pause()
        page.goto("https://demoqa.com/select-menu")
        # with page.expect_download() as download_info:
        #         page.locator("#downloadButton").click()
        # download = download_info.value
        # print(f"Downloaded file path: {download.path()}")
        # download.save_as("C:\\Users\\ADMIN\\Documents\\downloaded_file.png")

        page.locator("#cars").select_option(["Volvo","Audi","Saab"])
        options = page.locator("#cars option:checked").all_inner_texts()
        print("selected options:", options)
        # options = options[0].split("\n")
        options.remove("Volvo")
        print(options)
        page.locator("#cars").select_option(options)


        # page.locator("#cars").select_option(["Volvo"])
        # page.locator("#downloadButton")
        # page.locator("#cars").select_option([])
        # page.locator("#downloadButton")
        # page.locator("#oldSelectMenu").select_option(index= 6)
        # page.locator("#oldSelectMenu").select_option(value = "2")

        # page.locator("//*[text()='Main Item 2']").hover()
        # page.locator("//*[text()='Sub Item']").click(timeout=5000)
        time.sleep(5)



        # page.fill("locartor","value")
        # page.locator().click()
        # page.click() or check and uncheck()
        # page.click()
        # page.locator().dblclick()
        # page.locator().click(button="right")
        # page.locator("#uploadFile").set_input_files("C:\\Users\\ADMIN\\Documents\\test1.txt")
        # page.locator("#downloadButton").click()
        #
        # page.locator("#downloadButton").click()
        # page.bring_to_front()
        # page.locator("#tabButton").click()
        # time.sleep(2)
        # print(context.pages)



        # print(context.pages())
        # print(pages)
        # print(len(pages))


        # page.locator("//*[text()='Click Me']").click()
        # page.locator("#doubleClickBtn").dblclick()
        # page.locator("#rightClickBtn").click(button="right")
        # page.fill("#userName","testuser")
        # page.locator("#userEmail").fill("name@gmail")
        # page.fill("#currentAddress","1 corss bangalore 560055")
        # page.fill("#permanentAddress","1 corss bangalore 560055")
        # page.locator("#submit").click(timeout=5*000)
        # checkbox = page.locator("[aria-label='Select Home']")
        # # checkbox.click()
        # # assert checkbox.is_checked() == True, "Checkbox is not checked"
        # checkbox.uncheck()
        # assert checkbox.is_checked() == False, "Checkbox is still checked"

        # page.close()


# def test_newcase():
#         with sync_playwright() as p:
#                 # 1. Choose your device configuration
#                 iphone_14 = p.devices["iPhone 14"]
#
#                 browser = p.chromium.launch(headless=False)
#
#                 # 2. Unpack the device settings into a new context
#                 context = browser.new_context(**iphone_14)
#
#                 page = context.new_page()
#                 page.goto("https://whatismybrowser.com")
#
#                 # Take a screenshot to see the mobile viewport layout
#                 page.screenshot(path="mobile_view.png")
#
#                 context.close()
#                 browser.close()
