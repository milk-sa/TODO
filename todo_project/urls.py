from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('', include('todo_app.urls')),  # Include your app’s urls
]
