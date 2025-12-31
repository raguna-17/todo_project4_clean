# api_views.py
from rest_framework import viewsets,generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('order')  # 並び替え反映
    serializer_class = TaskSerializer

    @action(detail=False, methods=['post'])
    def reorder(self, request):
        """
        並び替え用のカスタムアクション。
        JSONで送られたID順に Task.order を更新する
        """
        order = request.data.get('order', [])
        for idx, task_id in enumerate(order):
            Task.objects.filter(id=task_id).update(order=idx)
        return Response({"status": "ok"})

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer