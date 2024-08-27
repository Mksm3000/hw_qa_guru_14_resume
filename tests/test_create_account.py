import allure

from pages.account_page import account_page
from pages.main_page import main_page
from pages.registration_page import registration_page
from user.random import random_user


@allure.feature('User Registration')
@allure.title('Test account creation success')
def test_account_creation_form():
    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step('Находим и нажимаем кнопку создать аккаунт'):
        main_page.find_link_by_text_and_click('Create an Account')
        main_page.text_should_be_on_page('Create New Customer Account')

    with allure.step('Заполняем форму для случайного пользователя'):
        registration_page.fill_first_name(random_user.first_name)
        registration_page.fill_last_name(random_user.last_name)
        registration_page.fill_email(random_user.email)
        registration_page.fill_password(random_user.password)
        registration_page.fill_password_confirmation(random_user.password)
        registration_page.submit()

    with allure.step('Проверяем успешную регистрацию на странице аккаунта'):
        account_page.should_have_registered_user_with(
            f'{random_user.first_name} {random_user.last_name}')
