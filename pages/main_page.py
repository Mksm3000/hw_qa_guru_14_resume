from selene import browser, by, have


class MainPage:

    def open(self):
        browser.open('')

    def find_link_by_text_and_click(self, value):
        browser.element(by.link_text(value)).click()

    def find_size_and_click(self, value: str):
        browser.element(f"[option-label={value}]").click()

    def find_color_and_click(self, value):
        browser.element(f"[aria-label={value}]").click()

    def add_to_cart(self):
        browser.element('#product-addtocart-button').click()

    def confirm_adding_to_cart(self, value):
        browser.element('.page.messages').with_(timeout=10).should(have.exact_text(
            f'You added {value} to your shopping cart.'))

    def find_links_in_dropdown_menu(self, *value: tuple):
        nav_level_0 = browser.element(by.link_text(value[0]))
        nav_level_0.hover()
        nav_level_1 = browser.element(by.link_text(value[1]))
        if len(value) == 3:
            nav_level_1.hover()
            nav_level_2 = browser.element(by.link_text(value[2]))
            nav_level_2.click()
        else:
            nav_level_1.click()

    def text_should_be_on_page(self, value):
        browser.element(".base").should(have.exact_text(value))


main_page = MainPage()
