from playwright.sync_api import expect

from pages.users.user_page import UserPage
from pages.users.users_page import UsersPage
from utils.data_generator import generate_user_params


class UserStep:
    """Шаги для пользователя."""

    def __init__(self, user_page: UserPage, users_page: UsersPage) -> None:
        self.user_page = user_page
        self.users_page = users_page

    def click_users_button(self) -> None:
        self.users_page.users_button().click()
        expect(self.users_page.table()).to_be_visible()

    def click_create_button(self) -> None:
        self.user_page.create_button().click()
        expect(self.user_page.first_name_field()).to_be_visible()

    def fill_email(self, email: str = None) -> str:
        email = email or generate_user_params()[0]
        self.user_page.user_email_field().fill(email)
        return email

    def fill_first_name(self) -> str:
        first_name = generate_user_params()[1]
        self.user_page.first_name_field().fill(first_name)
        return first_name

    def fill_last_name(self) -> str:
        last_name = generate_user_params()[2]
        self.user_page.last_name_field().fill(last_name)
        return last_name

    def click_save_button(self) -> None:
        self.user_page.save_button().click()
        expect(self.user_page.element_created()).to_be_visible()

    def click_save_button_for_edit(self) -> None:
        self.user_page.save_button().click()

    def check_user_in_table(self, email: str, first_name: str, last_name: str) -> None:
        expect(self.users_page.table_row_by_field(email)).to_contain_text(first_name)
        expect(self.users_page.table_row_by_field(email)).to_contain_text(last_name)

    def create_user(self) -> tuple[str, str, str]:
        self.click_create_button()
        email = self.fill_email()
        first_name = self.fill_first_name()
        last_name = self.fill_last_name()
        self.click_save_button()
        return email, first_name, last_name

    def get_users(self) -> None:
        expect(self.users_page.email_header()).to_be_visible()
        expect(self.users_page.last_name_header()).to_be_visible()
        expect(self.users_page.first_name_header()).to_be_visible()
        expect(self.users_page.table_row()).to_have_count(9)

    def click_first_user(self) -> str:
        email = self.users_page.user_row_email()
        first_name = self.users_page.user_row_first_name()
        last_name = self.users_page.user_row_last_name()
        self.users_page.table_row().nth(1).click()
        expect(self.user_page.user_email_field()).to_have_value(email)
        expect(self.user_page.first_name_field()).to_have_value(first_name)
        expect(self.user_page.last_name_field()).to_have_value(last_name)
        return email

    def edit_user(self) -> tuple[str, str, str]:
        self.click_first_user()
        email = self.fill_email()
        first_name = self.fill_first_name()
        last_name = self.fill_last_name()
        self.click_save_button_for_edit()
        expect(self.user_page.element_updated()).to_be_visible()
        return email, first_name, last_name

    def edit_user_wrong_email(self) -> None:
        self.click_first_user()
        self.fill_email("wrong_email")
        self.click_save_button_for_edit()
        expect(self.user_page.wrong_email_message()).to_be_visible()

    def click_delete_button(self, email: str, email_2: str = None) -> None:
        self.user_page.delete_button().click()
        expect(self.users_page.table_row_by_field(email)).not_to_be_visible()
        if email_2:
            expect(self.users_page.table_row_by_field(email_2)).not_to_be_visible()

    def delete_user(self) -> str:
        email = self.click_first_user()
        self.click_delete_button(email)

    def click_first_user_checkbox(self) -> str:
        email = self.users_page.user_row_email(1)
        self.users_page.table_row_checkbox(1).click()
        return email

    def click_second_user_checkbox(self) -> str:
        email = self.users_page.user_row_email(2)
        self.users_page.table_row_checkbox(2).click()
        return email

    def delete_multiple_users(self) -> str:
        email = self.click_first_user_checkbox()
        email_2 = self.click_second_user_checkbox()
        self.click_delete_button(email, email_2)
