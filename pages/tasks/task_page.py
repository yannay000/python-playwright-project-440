from playwright.sync_api import Locator, Page

from pages.header_page import HeaderPage
from pages.left_menu_page import LeftMenuPage


class TaskPage(LeftMenuPage, HeaderPage):
    """Страница задачи."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def assignee_listbox(self) -> Locator:
        return self.page.get_by_role("combobox", name="Assignee")

    def title_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Title")

    def status_listbox(self) -> Locator:
        return self.page.get_by_role("combobox", name="Status")

    def list_items(self) -> Locator:
        return self.page.get_by_role("listbox").get_by_role("option")

    def email_link(self, email: str) -> Locator:
        return self.page.get_by_role("link", name=email)
