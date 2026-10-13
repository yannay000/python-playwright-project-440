from playwright.sync_api import Locator, Page

from pages.header_page import HeaderPage
from pages.left_menu_page import LeftMenuPage
from pages.table_page import TablePage


class UsersPage(LeftMenuPage, HeaderPage, TablePage):
    """Страница пользователей."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def email_header(self) -> Locator:
        return self.table().get_by_label("Sort by email")

    def last_name_header(self) -> Locator:
        return self.table().get_by_label("Sort by last name")

    def first_name_header(self) -> Locator:
        return self.table().get_by_label("Sort by first name")

    def user_row_email(self, index: int = 1) -> Locator:
        return self.table_row().nth(index).get_by_role("cell").nth(2).text_content()

    def user_row_first_name(self) -> Locator:
        return self.table_row().get_by_role("cell").nth(3).text_content()

    def user_row_last_name(self) -> Locator:
        return self.table_row().get_by_role("cell").nth(4).text_content()
