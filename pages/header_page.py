# pages/header_page.py
from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class HeaderPage(BasePage):
    """Страница заголовка."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def profile_button(self) -> Locator:
        return self.page.get_by_label("Profile")

    def logout_button(self) -> Locator:
        return self.page.get_by_text("Logout")
