# steps/login_step.py
import allure
from playwright.sync_api import expect

from pages.header_page import HeaderPage
from pages.login_page import LoginPage


class HeaderStep:
    """Шаги для логина."""
    def __init__(self, login_page: LoginPage, header_page: HeaderPage) -> None:
        self.login_page = login_page
        self.header_page = header_page

    @allure.step("Открыть страницу c заголовком.")
    def open(self) -> None:
        """Открыть страницу c заголовком."""
        self.header_page.open()
        expect(self.header_page.profile_button()).to_be_visible()

    @allure.step("Выйти из аккаунта.")
    def logout(self) -> None:
        """Выйти из аккаунта."""
        self.header_page.profile_button().click()
        self.header_page.page.set_viewport_size({"width": 1920, "height": 1080})
        self.header_page.logout_button().click()
        expect(self.login_page.username_field()).to_be_visible()
