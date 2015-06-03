# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_thread', models.TextField(null=True, blank=True)),
                ('news_title', models.TextField(null=True, blank=True)),
                ('news_url', models.TextField(null=True, blank=True)),
                ('news_time', models.TextField(null=True, blank=True)),
                ('news_from', models.TextField(null=True, blank=True)),
                ('from_url', models.TextField(null=True, blank=True)),
                ('news_body', models.TextField(null=True, blank=True)),
                ('dele', models.BooleanField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
