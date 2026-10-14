# tests/test_status.py
from typing import Callable

import pytest
from playwright.sync_api import Page

from pages.statuses.status_page import StatusPage
from pages.statuses.statuses_page import StatusesPage
from steps.status_step import StatusStep


@pytest.fixture
def status_page(page: Page) -> StatusPage:
    return StatusPage(page)


@pytest.fixture
def statuses_page(page: Page) -> StatusesPage:
    return StatusesPage(page)


def test_status_create_successfully(
	open_main_page: Callable, status_page: StatusPage, statuses_page: StatusesPage
	) -> None:
    status_step = StatusStep(status_page, statuses_page)
    status_step.click_statuses_button()
    name, slug = status_step.create_status()
    status_step.click_statuses_button()
    status_step.check_status_in_table(name, slug)


def test_status_get_successfully(
	open_main_page: Callable, status_page: StatusPage, statuses_page: StatusesPage
	) -> None:
    status_step = StatusStep(status_page, statuses_page)
    status_step.click_statuses_button()
    status_step.get_statuses()


def test_status_edit_successfully(
	open_main_page: Callable, status_page: StatusPage, statuses_page: StatusesPage
) -> None:
    status_step = StatusStep(status_page, statuses_page)
    status_step.click_statuses_button()
    name, slug = status_step.edit_status()
    status_step.check_status_in_table(name, slug)


def test_status_delete_successfully(
	open_main_page: Callable, status_page: StatusPage, statuses_page: StatusesPage
) -> None:
    status_step = StatusStep(status_page, statuses_page)
    status_step.click_statuses_button()
    status_step.delete_status()


def test_status_delete_multiple_successfully(
	open_main_page: Callable, status_page: StatusPage, statuses_page: StatusesPage
) -> None:
    status_step = StatusStep(status_page, statuses_page)
    status_step.click_statuses_button()
    status_step.delete_multiple_statuses()
