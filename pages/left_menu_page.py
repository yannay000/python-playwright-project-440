# pages/header_page.py
from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class LeftMenuPage(BasePage):
    """Страница левого меню."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def users_button(self) -> Locator:
        return self.page.get_by_text("Users")

    def statuses_button(self) -> Locator:
        return self.page.get_by_text("Task statuses")

    def labels_button(self) -> Locator:
        return self.page.get_by_text("Labels")

    def tasks_button(self) -> Locator:
        return self.page.get_by_text("Tasks")
