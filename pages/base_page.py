# tests/pages/base_page.py
from playwright.sync_api import Page

from config import APP_BASE_URL


class BasePage:
    """Базовый класс для всех Page Objects."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, path: str = "") -> None:
        """Открыть страницу по относительному пути."""
        self.page.goto(f"{APP_BASE_URL}/{path}")
