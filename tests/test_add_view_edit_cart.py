import allure

from pages.main_page import main_page
from pages.login_page import login_page
from pages.account_page import account_page
from user.given import given_user

@allure.feature('Cart functionality')
@allure.title('Test adding to cart, view and edit cart')
def test_adding_view_edit_cart():
    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step('Находим и нажимаем кнопку Sign In'):
        main_page.find_link_by_text_and_click('Sign In')
        main_page.text_should_be_on_page('Customer Login')

    with allure.step('Заполняем форму для уже зарегистрированного пользователя'):
        login_page.fill_email(given_user.email)
        login_page.fill_password(given_user.password)
        login_page.submit()

    with allure.step('Проверяем успешный вход на странице аккаунта'):
        account_page.should_have_registered_user_with(
            f'{given_user.first_name} {given_user.last_name}')

    with allure.step('Находим и нажимаем кнопку {Men}'):
        main_page.find_link_by_text_and_click('Men')
        main_page.text_should_be_on_page('Men')

    with allure.step('Находим и нажимаем кнопку {Jackets}'):
        main_page.find_link_by_text_and_click('Jackets')
        main_page.text_should_be_on_page('Jackets')

    with allure.step('Находим и нажимаем товар {Beaumont Summit Kit}'):
        main_page.find_link_by_text_and_click('Beaumont Summit Kit')
        main_page.text_should_be_on_page('Beaumont Summit Kit')

    with allure.step('Находим размер {XL} и кликаем'):
        main_page.find_size_and_click('XL')

    with allure.step('Находим цвет {Red} и кликаем'):
        main_page.find_color_and_click('Red')

    with allure.step('Нажимаем на кнопку {Add to Cart}'):
        main_page.add_to_cart()

    with allure.step(
            'Ожидаем сообщения на экране о добавлении {Beaumont Summit Kit} в корзину'):
        main_page.confirm_adding_to_cart('Beaumont Summit Kit')

    with allure.step('Находим кнопку {Men} наводим курсор, ищем кнопку {Bottoms} и '
                     'наводим курсор, ищем кнопку {Shorts} и кликаем'):
        main_page.find_links_in_dropdown_menu('Men', 'Bottoms', 'Shorts')
        main_page.text_should_be_on_page('Shorts')

    with allure.step('Находим и нажимаем товар {Torque Power Short}'):
        main_page.find_link_by_text_and_click('Torque Power Short')
        main_page.text_should_be_on_page('Torque Power Short')

    with allure.step('Находим размер {36} и кликаем'):
        main_page.find_size_and_click('36')

    with allure.step('Находим цвет {Purple} и кликаем'):
        main_page.find_color_and_click('Purple')

    with allure.step('Находим поле {QTY} и указываем количество товара {2}'):
        main_page.find_and_change_qty(2)

    with allure.step('Нажимаем на кнопку {Add to Cart}'):
        main_page.add_to_cart()

    with allure.step(
            'Ожидаем сообщения на экране о добавлении {Torque Power Short} в корзину'):
        main_page.confirm_adding_to_cart('Torque Power Short')

    with allure.step('Нажимаем на иконку {Checkout Cart}'):
        main_page.view_and_edit_cart()

    with allure.step('Ожидаем сообщения на экране {Shopping Cart}'):
        main_page.text_should_be_on_page('Shopping Cart')

    with allure.step(
            'В корзине для товара {Torque Power Short} изменяем количество на {1}'):
        main_page.find_item_and_edit_qty(item='Torque Power Short', qty='1')

    with allure.step('Для оформления заказа нажимаем на кнопку {Proceed to Checkout}'):
        main_page.find_button_by_text_and_click('Proceed to Checkout')

    with allure.step('Переходим на страницу оформления заказа, в коде должен быть текст {Checkout}'):
        main_page.text_should_be_on_page('Checkout')

