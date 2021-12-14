from django.db import models

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey('login_reg.User', related_name='messages', on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    message =models.ForeignKey(Message, related_name='message_comments', on_delete=models.CASCADE)
    user = models.ForeignKey('login_reg.User', related_name='comments', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Create your models here.
