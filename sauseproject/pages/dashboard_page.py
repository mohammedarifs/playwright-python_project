from playwright.sync_api import expect


class Dahboard_page:
    def __init__(self, page):
        self.page = page

    def assert_title(self, msg):
        assert self.page.title() == msg, "not able to login"

    def logout(self):
        self.page.get_by_text("Open Menu").click()
        self.page.get_by_text("Logout").click()

    def add_product(self):
        self.page.get_by_role("button",name="add-to-cart-sauce-labs-backpack").click()

    def click_checkout(self):
        self.page.locator("#shopping_cart_container>a").click()

    def verify_product_added(self):
        return expect(self.page.locator("//*[text()='Sauce Labs Backpack']")).to_be_visible()

