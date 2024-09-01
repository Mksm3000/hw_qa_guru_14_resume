from selene import browser, by, have, be


class MainPage:

    def open(self):
        browser.open('')

    def find_link_by_text_and_click(self, value):
        browser.element(by.link_text(value)).click()

    def find_size_and_click(self, value: str):
        browser.element(f"[option-label='{value}']").click()

    def find_color_and_click(self, value):
        browser.element(f"[aria-label={value}]").click()

    def find_and_change_qty(self, value):
        browser.element('#qty').set_value(value)

    def add_to_cart(self):
        browser.element('#product-addtocart-button').click()

    def confirm_adding_to_cart(self, value):
        browser.element('.page.messages').with_(timeout=10).should(have.exact_text(
            f'You added {value} to your shopping cart.'))

    # def view_and_edit_cart(self):
    #     browser.element('.action.showcart').click()
    #     browser.element('.action.showcart.active').should(be.visible)
    #     browser.element('.action.viewcart').click()

    def find_item_and_edit_qty(self, item, qty):
        required_item = browser.element(by.xpath(
            "//tr[@class='item-info']//a[@title='{item}' "
            "]//..//..//input[@class='input-text qty']".format(item=item)))
        required_item.set_value(qty)
        browser.element('.action.update').click()

    def find_button_by_text_and_click(self, value):
        button = browser.element(
            by.xpath("//button[@title='{value}']".format(value=value)))
        button.click()

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
        browser.element('.base').should(have.exact_text(value))

    def delete_all_from_cart(self):
        browser.element('.action.showcart').click()
        count = len(browser.all('.action.delete'))
        for _ in range(count):
            browser.element('.action.delete').click()
            browser.element('.action-primary.action-accept').click()


main_page = MainPage()
