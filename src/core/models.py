from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, blank=True, null=True)
    started_at = models.DateTimeField('started at', auto_now_add=True)

class Spec(models.Model):
    code = models.TextField()
    session = models.ForeignKey(Session)
    author = models.ForeignKey(User, verbose_name='The author of this last update.')
    tests_passed = models.NullBooleanField(default=False)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'saved_at'
