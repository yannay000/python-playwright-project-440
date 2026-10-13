from playwright.sync_api import Locator, Page

from pages.header_page import HeaderPage
from pages.left_menu_page import LeftMenuPage


class LabelPage(LeftMenuPage, HeaderPage):
    """Страница лейблов."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def label_name_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Name")
