# Generated by Django 2.2.3 on 2020-02-26 14:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('user', 'message', 'photo')},
        ),
        migrations.RemoveField(
            model_name='post',
            name='message_html',
        ),
        migrations.RemoveField(
            model_name='post',
            name='music',
        ),
    ]
