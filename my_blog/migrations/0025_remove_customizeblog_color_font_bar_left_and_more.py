# Generated by Django 4.2.6 on 2024-05-09 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0024_customizeblog_background_gradient_color_head_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customizeblog',
            name='color_font_bar_left',
        ),
        migrations.RemoveField(
            model_name='customizeblog',
            name='color_font_bar_right',
        ),
        migrations.RemoveField(
            model_name='customizeblog',
            name='color_font_footer',
        ),
    ]
