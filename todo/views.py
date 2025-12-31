from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskReorderView(APIView):
    def post(self, request):
        order = request.data.get('order', [])
        for index, task_id in enumerate(order):
            Task.objects.filter(id=task_id).update(order=index)
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)


# =========================
# タスク詳細・編集・削除 API（★追加）
# =========================
class TaskDetailAPI(APIView):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return Response({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
            "created_at": task.created_at,
        })

    def patch(self, request, pk):
        task = get_object_or_404(Task, pk=pk)

        task.title = request.data.get("title", task.title)
        task.description = request.data.get("description", task.description)
        task.completed = request.data.get("completed", task.completed)

        task.save()
        return Response({"status": "updated"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response({"status": "deleted"}, status=status.HTTP_204_NO_CONTENT)


# =========================
# 画面表示（従来通り）
# =========================
def index(request):
    # ※ 並び順は API と一致させる
    tasks = Task.objects.order_by('order', '-created_at')
    return render(request, 'todo/index.html', {'tasks': tasks})

