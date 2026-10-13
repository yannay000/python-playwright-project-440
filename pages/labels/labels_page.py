from playwright.sync_api import Locator, Page

from pages.header_page import HeaderPage
from pages.left_menu_page import LeftMenuPage
from pages.table_page import TablePage


class LabelsPage(LeftMenuPage, HeaderPage, TablePage):
    """Страница лейблов."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def name_header(self) -> Locator:
        return self.table().get_by_label("Sort by name")

    def label_row_name(self, index: int = 1) -> Locator:
        return self.table_row().nth(index).get_by_role("cell").nth(2).text_content()
