# The actual django version the  table auth.user is created and it adds to the adim
# automatically when we run python manage.py migrate
# Besides to create others models customized we follow the same process

from django.db import models
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf.global_settings import EMAIL_HOST_USER
from my_blog.models import CustomizeBlog

User = get_user_model()


class Notification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='notification')
    # The user don't have notifications by default
    has_notifications = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='Profile', blank=True, null=False)
    profession = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(null=True)
    birthday = models.DateField(null=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


"""
# Create your models here.
class Users(User):
    pass

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
"""


@receiver(post_save, sender=User)
def email(sender, instance, created, **kwargs):
    # My setting
    setting = CustomizeBlog.objects.get(active_setting=True) if len(
        CustomizeBlog.objects.filter(active_setting=True)) == 1 else CustomizeBlog.objects.filter(active_setting=True)
    subject = 'Welcome to MyDailyBlog'
    html_message = render_to_string('email/html_template.html', {'title': 'Welcome', 'welcome': 'welcome',
                                                                 'userregistered': instance.first_name + ' ' + instance.last_name,
                                                                 'webname': 'My Daily Routines','setting': setting, })
    plain_message = strip_tags(html_message)
    from_email = EMAIL_HOST_USER  # EMAIL_HOST_USER config('EMAIL_HOST_USER')
    to = instance.email
    if created:
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
