from playwright.sync_api import Locator, Page


class TablePage:
    """Страница таблицы."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def table(self) -> Locator:
        return self.page.get_by_role("table")

    def table_row(self) -> Locator:
        return self.table().get_by_role("row")

    def table_row_by_field(self, field: str) -> Locator:
        return self.table().get_by_role("row").filter(has_text=field)

    def table_row_checkbox(self, index: int) -> Locator:
        return self.table_row().nth(index).get_by_role("cell").nth(0)
