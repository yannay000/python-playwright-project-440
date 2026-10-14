# tests/test_task.py
from typing import Callable

import pytest
from playwright.sync_api import Page

from pages.tasks.task_page import TaskPage
from pages.tasks.tasks_page import TasksPage
from steps.task_step import TaskStep


@pytest.fixture
def task_page(page: Page) -> TaskPage:
    return TaskPage(page)


@pytest.fixture
def tasks_page(page: Page) -> TasksPage:
    return TasksPage(page)


def test_task_create_successfully(open_main_page: Callable, task_page: TaskPage, tasks_page: TasksPage) -> None:
    task_step = TaskStep(task_page, tasks_page)
    task_step.click_tasks_button()
    title, status = task_step.create_task()
    task_step.click_tasks_button()
    task_step.check_task_in_table(title, status)


def test_task_get_successfully(open_main_page: Callable, task_page: TaskPage, tasks_page: TasksPage) -> None:
    task_step = TaskStep(task_page, tasks_page)
    task_step.click_tasks_button()
    task_step.check_tasks_count()


def test_task_filter_by_assignee_successfully(
	open_main_page: Callable, task_page: TaskPage, tasks_page: TasksPage
) -> None:
    task_step = TaskStep(task_page, tasks_page)
    task_step.click_tasks_button()
    task_step.filter_tasks_by_assignee()


def test_task_filter_by_label_successfully(
	open_main_page: Callable, task_page: TaskPage, tasks_page: TasksPage
) -> None:
    task_step = TaskStep(task_page, tasks_page)
    task_step.click_tasks_button()
    task_step.filter_tasks_by_label()


def test_task_filter_by_status_successfully(
	open_main_page: Callable, task_page: TaskPage, tasks_page: TasksPage
	) -> None:
    task_step = TaskStep(task_page, tasks_page)
    task_step.click_tasks_button()
    task_step.filter_tasks_by_status()


def test_task_edit_successfully(open_main_page: Callable, task_page: TaskPage, tasks_page: TasksPage) -> None:
    task_step = TaskStep(task_page, tasks_page)
    task_step.click_tasks_button()
    title, status = task_step.edit_task()
    task_step.check_task_in_table(title, status)


def test_task_move_successfully(open_main_page: Callable, task_page: TaskPage, tasks_page: TasksPage) -> None:
    tasks_page.page.set_viewport_size({"width": 1280, "height": 720})
    task_step = TaskStep(task_page, tasks_page)
    task_step.click_tasks_button()
    task_step.move_task()


def test_task_delete_successfully(open_main_page: Callable, task_page: TaskPage, tasks_page: TasksPage) -> None:
    task_step = TaskStep(task_page, tasks_page)
    task_step.click_tasks_button()
    task_step.delete_task()
