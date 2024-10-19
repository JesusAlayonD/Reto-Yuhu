from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from rest_framework import status
from .tasks import send_task_creation_email

class TaskView(APIView):
    def get(self, request):
        # Obtener todas las tareas
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Crear una nueva tarea
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_task_creation_email.delay(serializer.data['title'], serializer.data['email'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskUDView(APIView):
    def get(self, request, id):
        # Obtener una sola tarea
        try:
            task = Task.objects.get(id=id)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response({'error': 'Tarea no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        # Actualizar una sola tarea
        try:
            task = Task.objects.get(id=id)
            serializer = TaskSerializer(task, data=request.data)
            serializer.save()
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({'error': 'Tarea no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        # Eliminar una sola tarea
        try: 
            task = Task.objects.get(id=id)
            task.delete()
            return Response({'Post eliminado': task.title}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'error': 'Tarea no encontrada'} ,status=status.HTTP_404_NOT_FOUND)