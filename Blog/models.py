from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pub_date = models.DateTimeField(auto_now=True)
# Create your models here.
