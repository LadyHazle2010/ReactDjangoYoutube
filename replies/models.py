from django.db import models
from comments.models import Comment

class Reply(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'auth.User', related_name='replies', on_delete=models.CASCADE)
    comment = models.ForeignKey(
        'comments.Comment', related_name='replies', on_delete=models.CASCADE)
    text = models.CharField(max_length=300, blank=True, default='')


class Meta:
    ordering = ['created']
    class Meta:
        ordering = ['created']
