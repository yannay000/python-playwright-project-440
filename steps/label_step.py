from playwright.sync_api import expect

from pages.labels.label_page import LabelPage
from pages.labels.labels_page import LabelsPage
from utils.data_generator import generate_status_params


class LabelStep:
    """Шаги для статуса."""

    def __init__(self, label_page: LabelPage, labels_page: LabelsPage) -> None:
        self.label_page = label_page
        self.labels_page = labels_page

    def click_labels_button(self) -> None:
        self.labels_page.labels_button().click()
        expect(self.labels_page.table()).to_be_visible()

    def click_create_button(self) -> None:
        self.label_page.create_button().click()
        expect(self.label_page.label_name_field()).to_be_visible()

    def fill_name(self, name: str = None) -> str:
        name = name or generate_status_params()[0]
        self.label_page.label_name_field().fill(name)
        return name

    def click_save_button(self) -> None:
        self.label_page.save_button().click()
        expect(self.label_page.element_created()).to_be_visible()

    def click_save_button_for_edit(self) -> None:
        self.label_page.save_button().click()

    def check_label_in_table(self, name: str) -> None:
        expect(self.labels_page.table_row_by_field(name)).to_be_visible()

    def create_label(self) -> str:
        self.click_create_button()
        name = self.fill_name()
        self.click_save_button()
        return name

    def get_labels(self) -> None:
        expect(self.labels_page.name_header()).to_be_visible()
        expect(self.labels_page.table_row()).to_have_count(6)

    def click_first_label(self) -> str:
        name = self.labels_page.label_row_name()
        self.labels_page.table_row().nth(1).click()
        expect(self.label_page.label_name_field()).to_have_value(name)
        return name

    def edit_label(self) -> tuple[str]:
        self.click_first_label()
        name = self.fill_name()
        self.click_save_button_for_edit()
        expect(self.label_page.element_updated()).to_be_visible()
        return name

    def click_delete_button(self, name: str) -> None:
        self.label_page.delete_button().click()
        expect(self.labels_page.table_row_by_field(name)).not_to_be_visible()

    def delete_label(self) -> str:
        name = self.click_first_label()
        self.click_delete_button(name)
