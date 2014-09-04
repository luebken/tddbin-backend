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


def generate_session_name(existing_names):
    start_at = 1
    new_name = DEFAULT_SESSION_NAME_PREFIX + str(start_at)
    while new_name in existing_names:
        start_at += 1
        new_name = DEFAULT_SESSION_NAME_PREFIX + str(start_at)
    return new_name


def get_session_name(name, existing_names):
    if name:
        return name
    return generate_session_name(existing_names)

class UntitledSessionNamesTests(TestCase):
    def test_get_first_session_name(self):
        existing_session_names = []
        expected_name = DEFAULT_SESSION_NAME_PREFIX + '1'
        self.assertEquals(get_session_name('', existing_session_names), expected_name)

    def test_get_second_session_name(self):
        existing_session_names = [DEFAULT_SESSION_NAME_PREFIX + '1']
        expected_name = DEFAULT_SESSION_NAME_PREFIX + '2'
        self.assertEquals(get_session_name('', existing_session_names), expected_name)

    def test_get_fourth_session_name(self):
        existing_session_names = [
            DEFAULT_SESSION_NAME_PREFIX + '1',
            DEFAULT_SESSION_NAME_PREFIX + '2',
            DEFAULT_SESSION_NAME_PREFIX + '3',
        ]
        expected_name = DEFAULT_SESSION_NAME_PREFIX + '4'
        self.assertEquals(get_session_name('', existing_session_names), expected_name)

class ExistingSessionNamesTests(TestCase):
    def test_get_given_name(self):
        session_name = 'my session name'
        self.assertEquals(get_session_name(session_name, []), session_name)

