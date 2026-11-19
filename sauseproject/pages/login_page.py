



class LoginPage:
    def __init__(self,page):
        self.page = page

    def launch_url(self):
        self.page.goto("https://www.saucedemo.com/")

    def enter_username(self,username):
        self.page.locator("[name='user-name']").fill(username)

    def enter_password(self,password):
        self.page.get_by_placeholder("Password").fill(password)

    def click_login(self,):
        self.page.get_by_role("button", name="Login").click()



