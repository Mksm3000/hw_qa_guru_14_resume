import allure

from pages.main_page import main_page


@allure.feature('Site navigation')
@allure.title('Test links opening by click success')
def test_open_links_by_click_success():
    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step("Находим и нажимаем кнопку {What's New}"):
        main_page.find_link_by_text_and_click("What's New")
        main_page.text_should_be_on_page("What's New")

    with allure.step('Находим и нажимаем кнопку {Women}'):
        main_page.find_link_by_text_and_click('Women')
        main_page.text_should_be_on_page('Women')

    with allure.step('Находим и нажимаем кнопку {Men}'):
        main_page.find_link_by_text_and_click('Men')
        main_page.text_should_be_on_page('Men')

    with allure.step('Находим и нажимаем кнопку {Gear}'):
        main_page.find_link_by_text_and_click('Gear')
        main_page.text_should_be_on_page('Gear')

    with allure.step('Находим и нажимаем кнопку {Training}'):
        main_page.find_link_by_text_and_click('Training')
        main_page.text_should_be_on_page('Training')

    with allure.step('Находим и нажимаем кнопку {Sale}'):
        main_page.find_link_by_text_and_click('Sale')
        main_page.text_should_be_on_page('Sale')
