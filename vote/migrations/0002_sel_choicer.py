# Generated by Django 3.2.12 on 2022-04-04 10:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sel',
            name='choicer',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
