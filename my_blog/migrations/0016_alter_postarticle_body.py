# Generated by Django 4.2.6 on 2024-04-26 15:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0015_notify_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postarticle',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
