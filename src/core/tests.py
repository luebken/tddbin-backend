# -*- coding: utf-8 -*-
from django.test import TestCase

from .models import Session
from .models import Spec

# if self.name == '':
#     names = Session.objects.filter(name__startswith=self.UNTITLED_PREFIX, user=self.user).only('name')
#     name_suffix = 1
#     if len(names):
#         names = [x.name for x in names]
#         names = [int(x.replace(self.UNTITLED_PREFIX, '')) for x in names if x.replace(self.UNTITLED_PREFIX, '').isdigit()]
#         names.sort()
#         name_suffix = names[-1] + 1
#     self.name = self.UNTITLED_PREFIX + str(name_suffix)
# super(Session, self).save(*args, **kwargs) # Call the "real" save() method.

def get_session_name():
    return 'Untitled 1'

class SessionNameTests(TestCase):
    def test_get_first_session_name(self):
        self.assertEquals(get_session_name(), 'Untitled 1')
