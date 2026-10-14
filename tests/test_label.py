# tests/test_label.py
from typing import Callable

import pytest
from playwright.sync_api import Page

from pages.labels.label_page import LabelPage
from pages.labels.labels_page import LabelsPage
from steps.label_step import LabelStep


@pytest.fixture
def label_page(page: Page) -> LabelPage:
    return LabelPage(page)


@pytest.fixture
def labels_page(page: Page) -> LabelsPage:
    return LabelsPage(page)


def test_label_create_successfully(open_main_page: Callable, label_page: LabelPage, labels_page: LabelsPage) -> None:
    label_step = LabelStep(label_page, labels_page)
    label_step.click_labels_button()
    name = label_step.create_label()
    label_step.click_labels_button()
    label_step.check_label_in_table(name)


def test_label_get_successfully(open_main_page: Callable, label_page: LabelPage, labels_page: LabelsPage) -> None:
    label_step = LabelStep(label_page, labels_page)
    label_step.click_labels_button()
    label_step.get_labels()


def test_label_edit_successfully(open_main_page: Callable, label_page: LabelPage, labels_page: LabelsPage) -> None:
    label_step = LabelStep(label_page, labels_page)
    label_step.click_labels_button()
    name = label_step.edit_label()
    label_step.check_label_in_table(name)


def test_label_delete_successfully(open_main_page: Callable, label_page: LabelPage, labels_page: LabelsPage) -> None:
    label_step = LabelStep(label_page, labels_page)
    label_step.click_labels_button()
    label_step.delete_label()
