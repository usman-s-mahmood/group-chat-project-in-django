from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatGroup(models.Model):
    group_name = models.CharField(
        max_length=255,
        unique=True,
        null=False
    )
    
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.group_name
    
class GroupMessage(models.Model):
    group = models.ForeignKey(
        ChatGroup,
        related_name='chat_messages',
        on_delete=models.CASCADE
    )
    body = models.TextField(
        null=False,
        blank=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author.username} | {self.body}'
    
    class Meta: 
        ordering = ['-created']