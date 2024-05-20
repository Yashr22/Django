from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SignupData(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=15)
    confirm_password = models.CharField(max_length=15)
    
class ContactMessage(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fullname
    
    
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'