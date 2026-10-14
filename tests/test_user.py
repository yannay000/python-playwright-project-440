# tests/test_login.py
from typing import Callable

import pytest
from playwright.sync_api import Page

from pages.users.user_page import UserPage
from pages.users.users_page import UsersPage
from steps.user_step import UserStep


@pytest.fixture
def user_page(page: Page) -> UserPage:
    return UserPage(page)


@pytest.fixture
def users_page(page: Page) -> UsersPage:
    return UsersPage(page)


def test_user_create_successfully(open_main_page: Callable, user_page: UserPage, users_page: UsersPage) -> None:
    user_step = UserStep(user_page, users_page)
    user_step.click_users_button()
    email, first_name, last_name = user_step.create_user()
    user_step.click_users_button()
    user_step.check_user_in_table(email, first_name, last_name)


def test_user_get_successfully(open_main_page: Callable, user_page: UserPage, users_page: UsersPage) -> None:
    user_step = UserStep(user_page, users_page)
    user_step.click_users_button()
    user_step.get_users()


def test_user_edit_successfully(open_main_page: Callable, user_page: UserPage, users_page: UsersPage) -> None:
    user_step = UserStep(user_page, users_page)
    user_step.click_users_button()
    email, first_name, last_name = user_step.edit_user()
    user_step.check_user_in_table(email, first_name, last_name)


def test_user_edit_wrong_email(open_main_page: Callable, user_page: UserPage, users_page: UsersPage) -> None:
    user_step = UserStep(user_page, users_page)
    user_step.click_users_button()
    user_step.edit_user_wrong_email()


def test_user_delete_successfully(open_main_page: Callable, user_page: UserPage, users_page: UsersPage) -> None:
    user_step = UserStep(user_page, users_page)
    user_step.click_users_button()
    user_step.delete_user()


def test_user_delete_multiple_successfully(
	open_main_page: Callable, user_page: UserPage, users_page: UsersPage
) -> None:
    user_step = UserStep(user_page, users_page)
    user_step.click_users_button()
    user_step.delete_multiple_users()
