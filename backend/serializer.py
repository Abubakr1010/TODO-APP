# serializers.py
from rest_framework import serializers
from .models import User, Task



# Signup Serializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['user_id','first_name','last_name','email','password']

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        print (user.first_name,user.password)
        return user
    
    def validate(self,data):
        user_id = data.get('user_id')
        email = data.get('email')

        if User.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError({"user_id": "User with this user id already exists"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "User with this email already exist"})
        
        return data
    

# Create Task Serializer
class CreateTask(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['task_id','user_id','text','status']


# View Task Serializer
class ViewTask(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['user_id','task_id','text','status','created']


# Delete Task Serializer
class DeleteTask(serializers.Serializer):


    user_id = serializers.IntegerField()
    task_id = serializers.IntegerField()


# Update Task Serializer
class UpdateTask(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['user_id','task_id','text']


# CompletedTask Serializer 
class CompletedTask(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['user_id','task_id','status']
    

# Single User Task Serializer     
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['user_id','task_id','text','status','created'] 

class SingleUserTasks(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True, source='task_set')

    class Meta:
        model = User
        fields = ['tasks']
    
    
    
    
    
    
    
    

