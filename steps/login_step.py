# steps/login_step.py
from playwright.sync_api import expect

from config import LOGIN, PASSWORD
from pages.header_page import HeaderPage
from pages.login_page import LoginPage


class LoginStep:
    """Шаги для логина."""
    def __init__(self, login_page: LoginPage, header_page: HeaderPage) -> None:
        self.login_page = login_page
        self.header_page = header_page

    def open(self) -> None:
        """Открыть страницу логина."""
        self.login_page.open()

    def login(self) -> None:
        """Логин."""
        self.login_page.username_field().fill(LOGIN)
        self.login_page.password_field().fill(PASSWORD)
        self.login_page.sign_in_button().click()
        expect(self.header_page.profile_button()).to_be_visible()
