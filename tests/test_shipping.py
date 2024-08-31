import allure

from pages.account_page import account_page
from pages.login_page import login_page
from pages.main_page import main_page
from pages.shipping_page import shipping_page
from user.given import given_user


@allure.feature('Shipping form')
@allure.title('Test filling new shipping form')
def test_fill_new_shipping_form():
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

    with allure.step('Открываем страницу заполнения формы для доставки'):
        shipping_page.open()

    with allure.step('Заполняем строку {First Name}'):
        shipping_page.fill_first_name(given_user.first_name)

    with allure.step('Заполняем строку {Last Name}'):
        shipping_page.fill_last_name(given_user.last_name)

    with allure.step('Заполняем строку {Company}'):
        shipping_page.fill_company(given_user.company)

    with allure.step('Заполняем строку {Street}'):
        shipping_page.fill_street(given_user.street)

    with allure.step('Заполняем строку {City}'):
        shipping_page.fill_city(given_user.city)

    with allure.step('Заполняем строку {Country}'):
        shipping_page.fill_country(given_user.country)

    with allure.step('Заполняем строку {State}'):
        shipping_page.fill_state(given_user.state)

    with allure.step('Заполняем строку {ZIPcode}'):
        shipping_page.fill_zipcode(given_user.zipcode)

    with allure.step('Заполняем строку {Phone}'):
        shipping_page.fill_phone(given_user.phone)

    with allure.step('Указываем метод доставки {Best Way}'):
        shipping_page.fill_method('Best Way')

    with allure.step('Нажимаем кнопку {Next}'):
        shipping_page.button_next()

    with allure.step('Проверяем заполнение формы для доставки'):
        shipping_page.should_have_shipping_with((given_user.first_name,
                                                given_user.last_name,
                                                given_user.street,
                                                given_user.city,
                                                given_user.state,
                                                given_user.zipcode,
                                                given_user.country,
                                                given_user.phone))

    with allure.step('Проверяем заполнение формы для доставки'):
        shipping_page.should_have_shipping_with((given_user.first_name,
                                                given_user.last_name,
                                                given_user.street,
                                                given_user.city,
                                                given_user.state,
                                                given_user.zipcode,
                                                given_user.country,
                                                given_user.phone))

    with allure.step('Нажимаем кнопку {Place Order}'):
        shipping_page.button_place_order()

    with allure.step('Проверяем успешное оформление заказа'):
        main_page.text_should_be_on_page('Thank you for your purchase!')


@allure.feature('Shipping form')
@allure.title('Test filling existing shipping form')
def test_fill_existing_shipping_form():
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

    with allure.step('Открываем страницу заполнения формы для доставки'):
        shipping_page.open()

    with allure.step('Проверяем правильность ранее заполненной формы для доставки'):
        shipping_page.should_have_shipping_with_exist((given_user.first_name,
                                                      given_user.last_name,
                                                      given_user.street,
                                                      given_user.city,
                                                      given_user.state,
                                                      given_user.zipcode,
                                                      given_user.country,
                                                      given_user.phone))

    with allure.step('Указываем метод доставки {Best Way}'):
        shipping_page.fill_method('Best Way')

    with allure.step('Нажимаем кнопку {Next}'):
        shipping_page.button_next()

    with allure.step('Проверяем правильность ранее заполненной формы для доставки'):
        shipping_page.should_have_shipping_with_exist((given_user.first_name,
                                                      given_user.last_name,
                                                      given_user.street,
                                                      given_user.city,
                                                      given_user.state,
                                                      given_user.zipcode,
                                                      given_user.country,
                                                      given_user.phone))

    with allure.step('Нажимаем кнопку {Place Order}'):
        shipping_page.button_place_order()

    with allure.step('Проверяем успешное оформление заказа'):
        main_page.text_should_be_on_page('Thank you for your purchase!')
