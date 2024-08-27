from selene import browser, have


class RegistrationPage:

    def open(self):
        browser.open('customer/account/create/')

    def fill_first_name(self, value):
        browser.element('#firstname').type(value)

    def fill_last_name(self, value):
        browser.element('#lastname').type(value)

    def fill_email(self, value):
        browser.element('#email_address').type(value)

    def fill_password(self, value):
        browser.element('#password').type(value)

    def fill_password_confirmation(self, value):
        browser.element('#password-confirmation').type(value)

    def submit(self):
        browser.element('.action.submit.primary').click()

    def should_have_registered_user_with(self, value):
        browser.element('.logged-in').should(have.exact_texts(value))


registration_page = RegistrationPage()
