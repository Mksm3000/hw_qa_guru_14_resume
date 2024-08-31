from selene import browser, by, be, have


class ShippingPage:

    def open(self):
        browser.open('checkout/')

    def fill_first_name(self, value):
        browser.element('[name="firstname"]').type(value)

    def fill_last_name(self, value):
        browser.element('[name="lastname"]').type(value)

    def fill_company(self, value):
        browser.element('[name="company"]').type(value)

    def fill_street(self, value):
        browser.element('[name="street[0]"]').type(value)

    def fill_city(self, value):
        browser.element('[name="city"]').type(value)

    def fill_country(self, value):
        browser.element(by.xpath(
            "//select[@name='country_id']//option[@data-title='{value}']".format(
                value=value))).click()

    def fill_state(self, value):
        browser.element(by.xpath(
            "//select[@name='region_id']//option[@data-title='{value}']".format(
                value=value))).click()

    def fill_zipcode(self, value):
        browser.element('[name="postcode"]').set_value(value)

    def fill_phone(self, value):
        browser.element('[name="telephone"]').type(value)

    def fill_method(self, value):
        browser.element(by.xpath(
            "//td[@class='col col-carrier' and contains(text(), '{value}')]".format(
                value=value))).click()

    def button_next(self):
        browser.element('.button.action.continue.primary').click()

    def should_have_shipping_with(self, values: tuple):
        browser.element(by.xpath(
            "//div[@class='step-title' and contains(text(), 'Payment Method')]")).should(
            be.visible)
        for value in values:
            browser.element('.billing-address-details').should(have.text(value))

    def should_have_shipping_with_exist(self, values: tuple):
        for value in values:
            browser.element('.shipping-address-item.selected-item').should(
                have.text(value))

    def button_place_order(self):
        browser.element('.action.primary.checkout').click()


shipping_page = ShippingPage()
