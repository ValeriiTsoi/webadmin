from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=25, unique=True)
    role_id = models.IntegerField()
    description = models.CharField(max_length=150, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.username
