from playwright.sync_api import Locator, Page

from pages.header_page import HeaderPage
from pages.left_menu_page import LeftMenuPage


class UserPage(LeftMenuPage, HeaderPage):
    """Страница пользователя."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def first_name_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="First name")

    def user_email_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Email")

    def last_name_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Last name")

    def wrong_email_message(self) -> Locator:
        return self.page.get_by_text("Incorrect email format")
