from django.test import TestCase
from todo.models import Task
from django.urls import reverse
from rest_framework.test import APIClient

class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(title="テスト")
        self.assertEqual(task.title, "テスト")

class TodoViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task = Task.objects.create(title="既存タスク")

    def test_get_task_list(self):
        response = self.client.get(reverse("todo:todo-list"))
        self.assertEqual(response.status_code, 200)
        titles = [item["title"] for item in response.json()]
        self.assertIn("既存タスク", titles)

    def test_create_todo_via_api(self):
        response = self.client.post(
            reverse("todo:todo-list"),
            {"title": "新タスク"},
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Task.objects.filter(title="新タスク").exists())
