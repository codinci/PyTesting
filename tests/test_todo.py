import pytest
from pylenium.driver import Pylenium
from pylenium.element import Element, Elements

class TodoPage:
    def __init__(self, py: Pylenium):
        self.py = py

    def goto(self) -> 'TodoPage':
        self.py.visit('https://lambdatest.github.io/sample-todo-app/')
        return self

    def get_todo_by_name(self, name: str) -> Element:
        return self.py.getx(f"//*[text()='{name}']").parent()

    def get_all_todos(self) -> Elements:
        return self.py.find("li[ng-repeat*='todo']")


@pytest.fixture
def page(py: Pylenium):
    return TodoPage(py).goto()


def test_check_first_item(page: TodoPage):
    checkbox = page.get_todo_by_name('First Item').get('input')
    checkbox.click()
    assert checkbox.should().be_checked()

def test_check_many_items(py: Pylenium, page: TodoPage):
    todos = page.get_all_todos
    todo2, todo4 = todos[1], todos[3]
    todo2.get('input').click()
    todo4.get('input').click()
    assert py.contains('3 of 5 remaining')

def test_check_all_items(py: Pylenium, page: TodoPage):
    for todo in page.get_all_todos():
        todo.get('input').click()

    assert py.contains('0 of 5 remaining')