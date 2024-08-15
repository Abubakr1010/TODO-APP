from .common import *


DEBUG = True


SECRET_KEY = 'django-insecure-j=#q25ky5e(o(!6)^n5js74(qfk$ed1xr9u_(&p064ao96#x9b'


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'todo',    # Replace with your database name
        'USER': 'root',   # Replace with your MySQL username
        'PASSWORD': 'abubakr9',  # Replace with your MySQL password
        'HOST': 'localhost',            # Replace with your MySQL host, if necessary
        'PORT': '3306',                 # Replace with your MySQL port, if necessary
    }
}
