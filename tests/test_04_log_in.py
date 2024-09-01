import allure

from pages.account_page import account_page
from pages.login_page import login_page
from pages.main_page import main_page
from user.given import given_user
from user.nonexistent import nonexist_user


@allure.feature('User sign in')
@allure.title('Test signin successful')
def test_sign_in_form_successful():
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


@allure.feature('User sign in')
@allure.title('Test signin unsuccessful')
def test_sign_in_form_unsuccessful():
    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step('Находим и нажимаем кнопку Sign In'):
        main_page.find_link_by_text_and_click('Sign In')
        main_page.text_should_be_on_page('Customer Login')

    with allure.step('Заполняем форму для незарегистрированного пользователя'):
        login_page.fill_email(nonexist_user.email)
        login_page.fill_password(nonexist_user.password)
        login_page.submit()

    with allure.step('Проверяем сообщение об ошибке на странице входа в аккаунт'):
        login_page.should_have_unregistered_user_with(
            'The account sign-in was incorrect or your account is disabled '
            'temporarily. Please wait and try again later.')
