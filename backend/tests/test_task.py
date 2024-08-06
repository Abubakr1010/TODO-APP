import pytest
from backend.models import User
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


