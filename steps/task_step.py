from playwright.sync_api import Locator, expect

from pages.tasks.task_page import TaskPage
from pages.tasks.tasks_page import TasksPage
from utils.data_generator import generate_task_params


class TaskStep:
    """Шаги для задачи."""

    def __init__(self, task_page: TaskPage, tasks_page: TasksPage) -> None:
        self.task_page = task_page
        self.tasks_page = tasks_page

    def click_tasks_button(self) -> None:
        self.tasks_page.tasks_button().click()
        expect(self.tasks_page.create_button()).to_be_visible()

    def click_create_button(self) -> None:
        self.task_page.create_button().click()

    def fill_assignee(self, index: int = 5) -> str:
        self.task_page.assignee_listbox().click()
        assignee = self.task_page.list_items().nth(index)
        assignee_text = assignee.text_content()
        assignee.click()
        expect(assignee).not_to_be_visible()
        return assignee_text

    def fill_title(self) -> str:
        title = generate_task_params()[1]
        self.task_page.title_field().fill(title)
        return title

    def fill_status(self, index: int = 3) -> str:
        self.task_page.status_listbox().click()
        status = self.task_page.list_items().nth(index)
        status_text = status.text_content()
        status.click()
        expect(status).not_to_be_visible()
        return status_text

    def click_save_button(self) -> None:
        self.task_page.save_button().click()
        expect(self.task_page.element_created()).to_be_visible()

    def click_save_button_for_edit(self) -> None:
        self.task_page.save_button().click()

    def check_task_in_table(self, title: str, status: str) -> None:
        expect(self.tasks_page.tasks().filter(has_text=title)).to_be_visible()
        expect(self.tasks_page.column(status).filter(has_text=title)).to_be_visible()

    def create_task(self) -> tuple[str, str, str]:
        self.click_create_button()
        self.fill_assignee()
        title = self.fill_title()
        status = self.fill_status()
        self.click_save_button()
        return title, status

    def get_tasks_list(self) -> list[Locator]:
        return self.tasks_page.show_buttons().all()

    def check_tasks_by_assignee(self, tasks_list: list[Locator], assignee: str) -> None:
        for task in tasks_list:
            task.click()
            expect(self.task_page.email_link(assignee)).to_be_visible()
            self.tasks_page.tasks_button().click()

    def check_tasks_by_label(self, tasks_list: list[Locator], label: str) -> None:
        for task in tasks_list:
            task.click()
            expect(self.task_page.email_link(label)).to_be_visible()
            self.tasks_page.tasks_button().click()

    def fill_label(self, index: int = 1) -> str:
        self.tasks_page.label_filter().click()
        label = self.task_page.list_items().nth(index)
        label_text = label.text_content()
        label.click()
        expect(self.tasks_page.add_filter_button()).to_be_visible()
        return label_text

    def check_tasks_count(self) -> list[Locator]:
        expect(self.tasks_page.tasks()).to_have_count(15)

    def filter_tasks_by_assignee(self) -> None:
        assignee = self.fill_assignee()
        expect(self.tasks_page.add_filter_button()).to_be_visible()
        tasks_list = self.get_tasks_list()
        self.check_tasks_by_assignee(tasks_list, assignee)

    def filter_tasks_by_label(self) -> None:
        label = self.fill_label()
        tasks_list = self.get_tasks_list()
        self.check_tasks_by_label(tasks_list, label)

    def filter_tasks_by_status(self) -> None:
        status = self.fill_status()
        expect(self.tasks_page.tasks()).to_have_count(3)
        expect(self.tasks_page.column(status).get_by_label("Show")).to_have_count(3)

    def click_first_task(self) -> str:
        task = self.tasks_page.tasks().nth(0)
        task_text = task.text_content()
        self.tasks_page.edit_button(task).click()
        return task_text

    def edit_task(self) -> tuple[str, str, str]:
        self.click_first_task()
        title = self.fill_title()
        status = self.fill_status()
        self.click_save_button_for_edit()
        expect(self.task_page.element_updated()).to_be_visible()
        return title, status

    def move_task(self) -> str:
        """Координаты для viewport 1280×720: первая карточка Draft и колонка Published."""
        title = self.tasks_page.tasks().nth(0).inner_text().split("\n", maxsplit=1)[0]
        page = self.tasks_page.page
        start_x, start_y = 354, 224
        page.mouse.move(start_x, start_y)
        page.mouse.down()
        # Короткий сдвиг включает перетаскивание, длинный прыжок библиотека игнорирует.
        page.mouse.move(start_x + 12, start_y + 8, steps=5)
        page.mouse.move(1166, 228, steps=15)
        page.mouse.up()
        expect(self.tasks_page.column(generate_task_params()[2]).filter(has_text=title)).to_be_visible()
        return title

    def click_delete_button(self, task: str) -> None:
        self.tasks_page.delete_button().click()
        expect(self.tasks_page.tasks().filter(has_text=task)).not_to_be_visible()

    def delete_task(self) -> str:
        task = self.click_first_task()
        self.click_delete_button(task)
