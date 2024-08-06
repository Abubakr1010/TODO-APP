from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password=password, **extra_fields)

class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True, validators=[MinValueValidator(1)])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Task(models.Model):
    task_id = models.CharField(primary_key=True, max_length=30)  
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)  
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.text



