# Generated by Django 4.2.6 on 2023-12-24 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_reply_comment_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='comment_id',
            new_name='comment_identity',
        ),
    ]
