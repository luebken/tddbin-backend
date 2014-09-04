# -*- coding: utf-8 -*-
from django.test import TestCase

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

DEFAULT_SESSION_NAME_PREFIX = 'Untitled '
def get_session_name(name, existing_names):
    if name:
        return name
    new_name = DEFAULT_SESSION_NAME_PREFIX + '1'
    if new_name in existing_names:
        new_name = DEFAULT_SESSION_NAME_PREFIX + '2'
    if new_name in existing_names:
        new_name = DEFAULT_SESSION_NAME_PREFIX + '4'
    return new_name

class UntitledSessionNamesTests(TestCase):
    def test_get_first_session_name(self):
        existing_session_names = []
        self.assertEquals(get_session_name('', existing_session_names), DEFAULT_SESSION_NAME_PREFIX + '1')

    def test_get_second_session_name(self):
        existing_session_names = [DEFAULT_SESSION_NAME_PREFIX + '1']
        self.assertEquals(get_session_name('', existing_session_names), DEFAULT_SESSION_NAME_PREFIX + '2')

    def test_get_fourth_session_name(self):
        existing_session_names = [
            DEFAULT_SESSION_NAME_PREFIX + '1',
            DEFAULT_SESSION_NAME_PREFIX + '2',
            DEFAULT_SESSION_NAME_PREFIX + '3',
        ]
        self.assertEquals(get_session_name('', existing_session_names), DEFAULT_SESSION_NAME_PREFIX + '4')

class ExistingSessionNamesTests(TestCase):
    def test_get_given_name(self):
        session_name = 'my session name'
        self.assertEquals(get_session_name(session_name, []), session_name)

