# -*- coding: utf-8 -*-
from django.test import TestCase

DEFAULT_SESSION_NAME_PREFIX = 'Untitled '

def generate_session_name(existing_names):
    if len(existing_names) == 0:
        return DEFAULT_SESSION_NAME_PREFIX + '1'

    used_postfixes = []
    for name in existing_names:
        name_left_over = name.replace(DEFAULT_SESSION_NAME_PREFIX, '')
        if name_left_over.isdigit():
            used_postfixes.append(int(name_left_over))
    used_postfixes.sort()
    new_postfix = used_postfixes[-1] + 1
    return DEFAULT_SESSION_NAME_PREFIX + str(new_postfix)

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

    def test_get_double_digit_session_name(self):
        existing_session_names = [
            DEFAULT_SESSION_NAME_PREFIX + '1',
            DEFAULT_SESSION_NAME_PREFIX + '21',
            DEFAULT_SESSION_NAME_PREFIX + '22',
        ]
        expected_name = DEFAULT_SESSION_NAME_PREFIX + '23'
        self.assertEquals(get_session_name('', existing_session_names), expected_name)

class ExistingSessionNamesTests(TestCase):
    def test_get_given_name(self):
        session_name = 'my session name'
        self.assertEquals(get_session_name(session_name, []), session_name)

