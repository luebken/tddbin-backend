from django.db import models
from django.contrib.auth.models import User

from util.session import get_or_generate_session_name
from util.session import DEFAULT_SESSION_NAME_PREFIX

class Session(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, blank=True, null=True)
    started_at = models.DateTimeField('started at', auto_now_add=True)

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        existing_session_names = Session.objects.filter(name__startswith=DEFAULT_SESSION_NAME_PREFIX, user=self.user).only('name')
        self.name = get_or_generate_session_name(self.name, existing_session_names)
        super(Session, self).save(*args, **kwargs) # Call the "real" save() method.


class Spec(models.Model):
    code = models.TextField()
    session = models.ForeignKey(Session)
    author = models.ForeignKey(User, verbose_name='The author of this last update.')
    tests_passed = models.NullBooleanField(default=False)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'saved_at'

    # On Python 3: def __str__(self):
    def __unicode__(self):
        # for the admin, to make code readable
        return self.code.split('\n')[0]
