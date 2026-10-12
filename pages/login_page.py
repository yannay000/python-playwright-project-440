# pages/login_page.py
from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница логина."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def username_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="username")

    def password_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="password")

    def sign_in_button(self) -> Locator:
        return self.page.get_by_role("button", name="Sign in")
