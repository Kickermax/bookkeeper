"""
Здесь содержатся тесты для виджета добавления расходов
"""
import pytest

from PyQt6.QtCore import Qt
from pytestqt.qtbot import QtBot

from bookkeeper.view.add_expense_widget import AddExpenseWidget


@pytest.fixture
def widget(qtbot: QtBot) -> AddExpenseWidget:
    widget = AddExpenseWidget()
    qtbot.addWidget(widget)
    return widget


def test_add_expense(qtbot: QtBot, widget: AddExpenseWidget):
    description_input = widget.description_edit
    category_input = widget.category_combo
    amount_input = widget.amount_edit
    add_button = widget.add_button

    widget.set_categories([(1, "Еда")])

    qtbot.keyClicks(description_input, "DragonBall")
    category_input.setCurrentIndex(0)
    qtbot.keyClicks(amount_input, "404")

    with qtbot.waitSignal(widget.expense_added, timeout=1000) as signal:
        qtbot.mouseClick(add_button, Qt.MouseButton.LeftButton)

    assert signal.args == ["DragonBall", "Еда", 404]

    assert description_input.text() == ""
    assert amount_input.text() == ""
    assert category_input.currentIndex() == 0


def test_add_button_disabled_if_fields_empty(qtbot: QtBot, widget: AddExpenseWidget):
    add_button = widget.add_button
    description_input = widget.description_edit
    category_input = widget.category_combo
    amount_input = widget.amount_edit

    assert not add_button.isEnabled()

    widget.set_categories([(1, "Еда")])
    category_input.setCurrentIndex(0)

    assert not add_button.isEnabled()

    qtbot.keyClicks(description_input, "DragonBall")
    assert not add_button.isEnabled()

    qtbot.keyClicks(amount_input, "12.99")
    assert add_button.isEnabled()


def test_invalid_amount_warning_with_zero_value(qtbot):
    widget = AddExpenseWidget()
    qtbot.addWidget(widget)

    widget.description_edit.setText("Test expense")
    widget.category_combo.setCurrentIndex(0)
    widget.amount_edit.setText("0")
    message_box = widget._on_add_button_clicked()

    assert message_box is not None


def test_invalid_amount_warning_with_negative_value(qtbot):
    widget = AddExpenseWidget()
    qtbot.addWidget(widget)

    widget.description_edit.setText("Test expense")
    widget.category_combo.setCurrentIndex(0)
    widget.amount_edit.setText("-10.00")
    message_box = widget._on_add_button_clicked()

    assert message_box is not None


def test_invalid_amount_warning_with_bad_format(qtbot):
    widget = AddExpenseWidget()
    qtbot.addWidget(widget)

    widget.description_edit.setText("Test expense")
    widget.category_combo.setCurrentIndex(0)
    widget.amount_edit.setText("sadasd")
    message_box = widget._on_add_button_clicked()

    assert message_box is not None


def test_category_list_is_set_correctly(qtbot):
    categories = [(1, "Еда"), (2, "Транспорт"), (3, "Жильё")]

    widget = AddExpenseWidget()
    widget.set_categories(categories)
    qtbot.addWidget(widget)

    combo_box = widget.category_combo

    assert combo_box.count() == 3
    assert combo_box.itemText(0) == "Еда"
    assert combo_box.itemText(1) == "Транспорт"
    assert combo_box.itemText(2) == "Жильё"
