# tests/test_login.py
import allure
import pytest

from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from steps.header_step import HeaderStep
from steps.login_step import LoginStep


@allure.parent_suite("Login-Logout")
@allure.suite("Login")
@allure.title("Simple login")
def test_login_simple(header_page: HeaderPage, login_page: LoginPage) -> None:
    # Тест начинается сразу с главной страницы — логин уже сделан
    header_step = HeaderStep(login_page, header_page)
    header_step.open()


@allure.parent_suite("Login-Logout")
@allure.suite("Login")
@allure.title("Full login")
@pytest.mark.browser_context_args(storage_state=None)
def test_login_full(header_page: HeaderPage, login_page: LoginPage) -> None:
	login_step = LoginStep(login_page, header_page)
	login_step.open()
	login_step.login()


@allure.parent_suite("Login-Logout")
@allure.suite("Logout")
@allure.title("Simple logout")
def test_logout(header_page: HeaderPage, login_page: LoginPage) -> None:
    header_step = HeaderStep(login_page, header_page)
    header_step.open()
    header_step.logout()
