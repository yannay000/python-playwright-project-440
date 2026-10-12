# tests/pages/base_page.py
from playwright.sync_api import Locator, Page

from config import APP_BASE_URL


class BasePage:
    """Базовый класс для всех Page Objects."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, path: str = "") -> None:
        """Открыть страницу по относительному пути."""
        self.page.goto(f"{APP_BASE_URL}/{path}")

    def create_button(self) -> Locator:
        return self.page.get_by_label("Create", exact=True)

    def save_button(self) -> Locator:
        return self.page.get_by_label("Save", exact=True)

    def element_created(self) -> Locator:
        return self.page.get_by_text("Element created")

    def element_updated(self) -> Locator:
        return self.page.get_by_text("Element updated")

    def delete_button(self) -> Locator:
        return self.page.get_by_label("Delete", exact=True)
