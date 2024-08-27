from selene import browser, have, by


class AccountPage:

    def should_have_registered_user_with(self, value):
        browser.element('.page-header').element('.logged-in').with_(timeout=10).should(
            have.text(value))


account_page = AccountPage()
