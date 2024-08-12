# views.py
from rest_framework import status, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UserSerializer,CreateTask, DeleteTask, ViewTask, UpdateTask, CompletedTask, SingleUserTasks
from django.contrib.auth import login as auth_login
from .models import Task, User
from django.contrib.auth import authenticate


@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if email is None or password is None:
        return Response({"error":"please provide both email and password"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error":"Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not user.check_password(password):
        return Response({"error":"Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not user.is_active:
        return Response({"error":"User is deactivated"}, status=status.HTTP_404_NOT_FOUND)
    
    
    return Response({"success":"Logged in successfully", "status":"Active"}, status=status.HTTP_200_OK)



@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        serializer = CreateTask(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Created": "Your task is created successfully"}, status=status.HTTP_201_CREATED)
        return Response({"Error": "Task not created", "Details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_task(request):
    if request.method == 'GET':
        task = Task.objects.all()
        serializer = ViewTask(task, many=True).data
        print(serializer)
        return Response(serializer,status=status.HTTP_200_OK)
    
    
    return Response({"status":"Failed"}, status=status.HTTP_400_BAD_REQUEST)





@api_view(['DELETE'])
def delete(request):
    if request.method == 'DELETE':
        serializer = DeleteTask(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            task_id = serializer.validated_data['task_id']

            if Task.objects.filter(user_id=user_id, task_id=task_id).exists():
                Task.objects.filter(user_id=user_id, task_id=task_id).delete()
                return Response({"Deleted": "Your task is deleted successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
            


@api_view(['PUT'])
def update(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({"error":'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UpdateTask(task,data=request.data)
    if serializer.is_valid():
        print(serializer)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
            
@api_view(['POST'])
def completed(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({"error":"Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CompletedTask(task, data=request.data, partial=True)
    if serializer.is_valid():
       serializer.save()
       print(serializer)
       return Response ({"updated":"Your task updated sucessfully"}, status=status.HTTP_200_OK)
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def view_single_user_tasks(request,pk):
    try:
        task = User.objects.prefetch_related('task_set').get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SingleUserTasks(task).data
        return Response(serializer,status=status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)

    



  
    

    





