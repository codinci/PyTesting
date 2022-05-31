from pylenium.driver import Pylenium


def test_check_first_item(py: Pylenium):
    py.visit('https://lambdatest.github.io/sample-todo-app/')
    checkbox = py.getx("//*[text()='First Item']").parent().get('input')
    checkbox.click()
    assert checkbox.should().be_checked()

def test_check_many_items(py: Pylenium):
    py.visit('https://lambdatest.github.io/sample-todo-app/')
    todos = py.find("li[ng-repeat*='todo']")
    todo2, todo4 = todos[1], todos[3]
    todo2.get('input').click()
    todo4.get('input').click()
    assert py.contains('3 of 5 remaining')