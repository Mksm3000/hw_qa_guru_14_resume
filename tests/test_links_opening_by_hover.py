import allure

from pages.main_page import main_page


@allure.feature('Site navigation')
@allure.title('Test links opening by hover success')
def test_open_links_by_hover_success():
    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step('Находим кнопку {Women} наводим курсор, ищем кнопку {Tops} и '
                     'наводим курсор, ищем кнопку {Jackets} и кликаем'):
        main_page.find_links_in_dropdown_menu('Women', 'Tops', 'Jackets')
        main_page.text_should_be_on_page('Jackets')

    with allure.step('Находим кнопку {Women} наводим курсор, ищем кнопку {Tops} и '
                     'наводим курсор, ищем кнопку {Bras & Tanks} и кликаем'):
        main_page.find_links_in_dropdown_menu('Women', 'Tops', 'Bras & Tanks')
        main_page.text_should_be_on_page('Bras & Tanks')

    with allure.step('Находим кнопку {Women} наводим курсор, ищем кнопку {Bottoms} и '
                     'наводим курсор, ищем кнопку {Shorts} и кликаем'):
        main_page.find_links_in_dropdown_menu('Women', 'Bottoms', 'Shorts')
        main_page.text_should_be_on_page('Shorts')

    with allure.step('Находим кнопку {Men} наводим курсор, ищем кнопку {Tops} и '
                     'наводим курсор, ищем кнопку {Hoodies & Sweatshirts} и кликаем'):
        main_page.find_links_in_dropdown_menu('Men', 'Tops', 'Hoodies & Sweatshirts')
        main_page.text_should_be_on_page('Hoodies & Sweatshirts')

    with allure.step('Находим кнопку {Men} наводим курсор, ищем кнопку {Tops} и '
                     'наводим курсор, ищем кнопку {Tees} и кликаем'):
        main_page.find_links_in_dropdown_menu('Men', 'Tops', 'Tees')
        main_page.text_should_be_on_page('Tees')

    with allure.step('Находим кнопку {Gear} наводим курсор, ищем кнопку {Fitness '
                     'Equipment} и кликаем'):
        main_page.find_links_in_dropdown_menu('Gear', 'Fitness Equipment')
        main_page.text_should_be_on_page('Fitness Equipment')

    with allure.step('Находим кнопку {Gear} наводим курсор, ищем кнопку {Watches} и '
                     'кликаем'):
        main_page.find_links_in_dropdown_menu('Gear', 'Watches')
        main_page.text_should_be_on_page('Watches')
