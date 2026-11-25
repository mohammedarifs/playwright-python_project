
url = "https://www.saucedemo.com/"


class LoginPage:
    def __init__(self,page):
        self.page = page
        self.username  = "[name='user-name']"
        self.password = "Password"
        self.login = "Login"

    def launch_url(self):
        self.page.goto(url)

    def enter_username(self,username):
        try:
            self.page.locator(self.username).fill(username)
        except:
            print("error")

    def enter_password(self,password):
        self.page.get_by_placeholder(self.password).fill(password)

    def click_login(self,):
        self.page.get_by_role("button", name=self.login).click()



