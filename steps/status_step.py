from playwright.sync_api import expect

from pages.statuses.status_page import StatusPage
from pages.statuses.statuses_page import StatusesPage
from utils.data_generator import generate_status_params


class StatusStep:
    """Шаги для статуса."""

    def __init__(self, status_page: StatusPage, statuses_page: StatusesPage) -> None:
        self.status_page = status_page
        self.statuses_page = statuses_page

    def click_statuses_button(self) -> None:
        self.statuses_page.statuses_button().click()
        expect(self.statuses_page.table()).to_be_visible()

    def click_create_button(self) -> None:
        self.status_page.create_button().click()
        expect(self.status_page.status_name_field()).to_be_visible()

    def fill_name(self, name: str = None) -> str:
        name = name or generate_status_params()[0]
        self.status_page.status_name_field().fill(name)
        return name

    def fill_slug(self, slug: str = None) -> str:
        slug = slug or generate_status_params()[1]
        self.status_page.status_slug_field().fill(slug)
        return slug

    def click_save_button(self) -> None:
        self.status_page.save_button().click()
        expect(self.status_page.element_created()).to_be_visible()

    def click_save_button_for_edit(self) -> None:
        self.status_page.save_button().click()

    def check_status_in_table(self, name: str, slug: str) -> None:
        expect(self.statuses_page.table_row_by_field(name)).to_contain_text(slug)

    def create_status(self) -> tuple[str, str]:
        self.click_create_button()
        name = self.fill_name()
        slug = self.fill_slug()
        self.click_save_button()
        return name, slug

    def get_statuses(self) -> None:
        expect(self.statuses_page.name_header()).to_be_visible()
        expect(self.statuses_page.slug_header()).to_be_visible()
        expect(self.statuses_page.table_row()).to_have_count(6)

    def click_first_status(self) -> str:
        name = self.statuses_page.status_row_name()
        slug = self.statuses_page.status_row_slug()
        self.statuses_page.table_row().nth(1).click()
        expect(self.status_page.status_name_field()).to_have_value(name)
        expect(self.status_page.status_slug_field()).to_have_value(slug)
        return name

    def edit_status(self) -> tuple[str, str]:
        self.click_first_status()
        name = self.fill_name()
        slug = self.fill_slug()
        self.click_save_button_for_edit()
        expect(self.status_page.element_updated()).to_be_visible()
        return name, slug

    def click_delete_button(self, name: str, slug: str = None) -> None:
        self.status_page.delete_button().click()
        expect(self.statuses_page.table_row_by_field(name)).not_to_be_visible()
        if slug:
            expect(self.statuses_page.table_row_by_field(slug)).not_to_be_visible()

    def delete_status(self) -> str:
        name = self.click_first_status()
        self.click_delete_button(name)

    def click_first_status_checkbox(self) -> str:
        name = self.statuses_page.status_row_name(1)
        self.statuses_page.table_row_checkbox(1).click()
        return name

    def click_second_status_checkbox(self) -> str:
        name = self.statuses_page.status_row_name(2)
        self.statuses_page.table_row_checkbox(2).click()
        return name

    def delete_multiple_statuses(self) -> str:
        name = self.click_first_status_checkbox()
        slug = self.click_second_status_checkbox()
        self.click_delete_button(name, slug)
