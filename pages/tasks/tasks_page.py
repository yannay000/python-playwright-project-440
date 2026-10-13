from playwright.sync_api import Locator, Page

from pages.header_page import HeaderPage
from pages.left_menu_page import LeftMenuPage
from pages.table_page import TablePage


class TasksPage(LeftMenuPage, HeaderPage, TablePage):
    """Страница задач."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def assignee_filter(self) -> Locator:
        return self.page.get_by_role("combobox", name="Assignee")

    def title_filter(self) -> Locator:
        return self.page.get_by_role("combobox", name="Title")

    def label_filter(self) -> Locator:
        return self.page.get_by_role("combobox", name="Label")

    def options(self) -> Locator:
        return self.page.get_by_role("listbox").get_by_role("option")

    def tasks(self) -> Locator:
        return self.page.get_by_role("button").filter(has_text="Task")

    def column(self, status: str) -> Locator:
        return self.page.locator(".MuiBox-root").filter(has_text=status).last

    def edit_button(self, task: Locator) -> Locator:
        return task.get_by_label("Edit")

    def show_buttons(self) -> Locator:
        return self.page.get_by_label("Show").filter(visible=True)

    def add_filter_button(self) -> Locator:
        return self.page.get_by_label("Add filter")
