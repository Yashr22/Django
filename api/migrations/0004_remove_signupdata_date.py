# Generated by Django 5.0.6 on 2024-05-14 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signupdata',
            name='date',
        ),
    ]
