# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('started_at', models.DateTimeField(auto_now_add=True, verbose_name=b'started at')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.TextField()),
                ('tests_passed', models.NullBooleanField(default=False)),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(verbose_name=b'The author of this last update.', to=settings.AUTH_USER_MODEL)),
                ('session', models.ForeignKey(to='core.Session')),
            ],
            options={
                'get_latest_by': 'saved_at',
            },
            bases=(models.Model,),
        ),
    ]
