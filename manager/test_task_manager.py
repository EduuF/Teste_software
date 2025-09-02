import pytest
import unittest
from task_manager import TaskManager

@pytest.fixture
def manager_instance():
    return TaskManager()

def test_add_task(manager_instance):
    task = manager_instance.add_task("Estudar Pytest", "Preparar o seminário")
    assert task["title"] == "Estudar Pytest"
    assert task["completed"] == False
    assert manager_instance.get_task(task["id"]) is not None

def test_add_task_not_pass(manager_instance):
    task = manager_instance.add_task("Estudar Pytest", "Preparar o seminário")
    assert task["title"] == "Estudar Pytest"
    assert task["completed"] == True
    assert manager_instance.get_task(task["id"]) is not None

def test_add_two_tasks(manager_instance):
    manager_instance.add_task("Tarefa 1", "Descrição da Tarefa 1")
    manager_instance.add_task("Tarefa 2", "Descrição da Tarefa 2")
    assert len(manager_instance.list_tasks()) == 2

def test_update_task_status(manager_instance):
    task = manager_instance.add_task("Fazer exercício", "Ir para a academia")
    updated = manager_instance.update_task_status(task["id"], True)
    assert updated == True
    assert manager_instance.get_task(task["id"])["completed"] == True

def test_delete_task(manager_instance):
    task = manager_instance.add_task("Ligar para a mãe", "Lembrar de ligar para a mãe")
    deleted = manager_instance.delete_task(task["id"])
    assert deleted == True
    assert manager_instance.get_task(task["id"]) is None

def test_a_test_for_coverage(manager_instance):
    assert manager_instance.get_task(999) is None


class TestTaskManagerUnittest(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task_unittest(self):
        task = self.manager.add_task("Comprar pão", "Na padaria")
        self.assertEqual(task["title"], "Comprar pão")
