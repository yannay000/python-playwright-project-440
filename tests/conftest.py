import os
from typing import Any, Generator

import pytest
from playwright.sync_api import Browser, Page

from config import APP_BASE_URL
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from steps.header_step import HeaderStep
from steps.login_step import LoginStep

AUTH_FILE = ".auth/user.json"


@pytest.fixture(scope="session")
def auth_file(browser: Browser) -> str:
    """
    Не более одного раза за весь прогон: залогиниться и сохранить состояние.
    Возвращает путь к файлу. Тесты, которые используют эту фикстуру,
    неявно требуют наличия auth-файла до своего запуска.
    """
    # Если файл уже есть — не логинимся повторно
    if os.path.exists(AUTH_FILE):
        return AUTH_FILE

    # Создаём временный контекст для логина
    context = browser.new_context()
    page = context.new_page()

    page.goto(APP_BASE_URL)
    LoginStep(LoginPage(page), HeaderPage(page)).login()
    # page.wait_for_url("**/inventory.html")

    # Сохраняем состояние в файл
    os.makedirs(os.path.dirname(AUTH_FILE), exist_ok=True)
    context.storage_state(path=AUTH_FILE)
    context.close()

    return AUTH_FILE


@pytest.fixture(scope="session")
def browser_context_args(
    browser_context_args: dict[str, Any], auth_file: str
) -> dict[str, Any]:
    """
    Дополняем параметры контекста storage_state-файлом.
    Зависимость от auth_file гарантирует, что файл создан до тестов.
    """
    return {
        **browser_context_args,
        "base_url": APP_BASE_URL,
        "storage_state": auth_file,
    }


@pytest.fixture
def header_page(page: Page) -> HeaderPage:
    return HeaderPage(page)


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def open_main_page(login_page: LoginPage, header_page: HeaderPage) -> Generator[None, None, None]:
    HeaderStep(login_page, header_page).open()
