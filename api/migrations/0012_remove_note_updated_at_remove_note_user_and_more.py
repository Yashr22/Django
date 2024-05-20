# Generated by Django 5.0.6 on 2024-05-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_note_created_at_note_updated_at_note_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
