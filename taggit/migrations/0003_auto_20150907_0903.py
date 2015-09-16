# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
                ('user', models.ForeignKey(verbose_name='User', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Tag group',
                'verbose_name_plural': 'Tag groups',
            },
        ),
        migrations.AddField(
            model_name='tag',
            name='user',
            field=models.ForeignKey(verbose_name='User', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='tag',
            name='group',
            field=models.ForeignKey(related_name='tags', verbose_name='Group', blank=True, to='taggit.TagGroup', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='taggroup',
            unique_together=set([('name', 'user')]),
        ),
    ]
