import pytest
from backend.models import User, Task
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db
def test_login_successfully():
    first_name = 'test'
    last_name = 'user'
    email = 'testuser@gmail.com'
    password = 'password123'
    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )
    
    client = APIClient()
    url = reverse('login')
    data = {
        'email': email,
        'password': password
    }
    
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['success']== 'Logged in successfully'
    assert response.data['status']== 'Active'


@pytest.mark.django_db
def test_login_with_wrong_password():
    first_name = 'test'
    last_name = 'user'
    email = 'testuser@gmail.com'
    password = 'password123'
    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )


    client = APIClient()
    url = reverse('login')
    data = {
        'email':email,
        'password': 'wrong_password'
    }

    response = client.post(url, data, format='json')


    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['error'] == 'Invalid email or password' 
  

@pytest.mark.django_db
def test_login_with_wrong_email():
    first_name = 'test'
    last_name = 'user'
    email = 'testuser@gmail.com'
    password = 'password123'


    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )

    client = APIClient()
    url = reverse('login')
    data = {
    'email':'wrong_email',
    'password': password
    }
    
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['error'] == 'Invalid email or password'

    

@pytest.mark.django_db
def test_create_task_completed():
    user = User.objects.create_user(first_name='test', 
                                    last_name='user', 
                                    email='testuser@gmail.com',
                                    password='password123'
                                    )


    client = APIClient()
    url = reverse('create_task')
    data = {
        'task_id':'1',
        'user_id':user.user_id,
        'text':'New task',
    }

    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['Created'] == 'Your task is created successfully'




