# Generated by Django 4.2.6 on 2024-05-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0023_remove_customizeblog_background_color_bar_left_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customizeblog',
            name='background_gradient_color_head',
            field=models.CharField(default='rgb(100, 100,100)', max_length=20),
        ),
        migrations.AlterField(
            model_name='customizeblog',
            name='background_color_head_footer',
            field=models.CharField(default='Black', max_length=20),
        ),
        migrations.AlterField(
            model_name='customizeblog',
            name='color_font_bar_left',
            field=models.CharField(default='Black', max_length=20),
        ),
        migrations.AlterField(
            model_name='customizeblog',
            name='color_font_bar_right',
            field=models.CharField(default='Black', max_length=20),
        ),
        migrations.AlterField(
            model_name='customizeblog',
            name='color_font_footer',
            field=models.CharField(default='Black', max_length=20),
        ),
        migrations.AlterField(
            model_name='customizeblog',
            name='color_font_head',
            field=models.CharField(default='White', max_length=20),
        ),
    ]
