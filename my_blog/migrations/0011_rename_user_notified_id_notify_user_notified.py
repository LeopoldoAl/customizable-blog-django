# Generated by Django 4.2.6 on 2024-03-11 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0010_remove_notify_article_commented'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notify',
            old_name='user_notified_id',
            new_name='user_notified',
        ),
    ]
