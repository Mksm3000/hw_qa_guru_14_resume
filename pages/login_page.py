from selene import browser, have


class LoginPage:

    def open(self):
        browser.open('customer/account/login/')

    def fill_email(self, value):
        browser.element('#email').type(value)

    def fill_password(self, value):
        browser.element('#pass').type(value)

    def submit(self):
        browser.element('.action.login.primary').click()

    def should_have_loggined_user_with(self, value):
        browser.element('.logged-in').should(have.exact_texts(value))

    def should_have_unregistered_user_with(self, value):
        browser.element('.page.messages').with_(timeout=10).should(have.text(value))


login_page = LoginPage()
