from django.contrib.auth.models import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()


class Code(models.Model):
    """ This model don't appear inside the admin page
        already we only need one object of this type,
        and will create una html view for it.
    """
    code_bar_lateral_up = models.TextField(blank=True)
    code_bar_lateral_down = models.TextField(blank=True)
    code_bar_lateral_footer = models.TextField(blank=True)


class PostArticle(models.Model):
    """ This model represents an article. """
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, max_length=255)
    image_of_head = models.ImageField(upload_to='PostArticle', blank=True, null=True)
    body = RichTextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # The views will show by default
    show_views = models.BooleanField(default=True)
    # We change the form how show us the date in the commentaries
    show_comment_with_date = models.BooleanField(default=True)
    # This field will appear in the basedate but not will appear on the admin page
    number_of_ping_backs = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class CustomizeBlog(models.Model):
    """
        Creating a model that it allows to the user to custumize
        the parts of more important of the blog, this will be
        an html view and only the superusers will can work it,
        it is not will be available in the administer page.
    """
    name = models.CharField(default='settings', max_length=255)
    title_of_blog = models.CharField(default="Daily Routines"
                                     , max_length=100)
    description_of_blog = models.TextField(default="In this blog I am going to talk about my daily routines."
                                           , max_length=300)
    ico_image_therty_by_therty_px = models.ImageField(upload_to='CustomizeBlog',
                                                      blank=True,
                                                      null=True)
    menu_image = models.ImageField(upload_to='CustomizeBlog', blank=True, null=True)
    logo_image = models.ImageField(upload_to='CustomizeBlog', blank=True, null=True)
    notification_image = models.ImageField(upload_to='CustomizeBlog', blank=True, null=True)
    profile_default_image = models.ImageField(upload_to='CustomizeBlog', blank=True, null=True)
    background_color_head_footer = models.CharField(default='Black', max_length=20)
    background_gradient_color_head = models.CharField(default='rgb(100, 100,100)', max_length=20)
    color_font_head = models.CharField(default='White', max_length=20)
    active_setting = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customize Blog'


class Rating(models.Model):
    value = models.FloatField()
    comment = models.CharField(max_length=400)
    article_id = models.ForeignKey(PostArticle, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    read = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    number_of_reply = models.IntegerField(default=0)

    def __str__(self):
        return self.user_id.username

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'


class Reply(models.Model):
    comment_identity = models.IntegerField(default=0)
    reply = models.CharField(max_length=400)
    article_id = models.ForeignKey(PostArticle, on_delete=models.CASCADE)
    rating_id = models.ForeignKey(Rating, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    read = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user_id.username

    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'


class Notify(models.Model):
    slug_image_user_that_commented = models.CharField(default='Nothing', max_length=200)
    data_of_message = models.CharField(max_length=400)
    user_that_commented = models.CharField(max_length=200)
    user_notified = models.ForeignKey(User, on_delete=models.CASCADE)
    count_notification = models.IntegerField(default=0)
    status_notification = models.BooleanField(default=False)
    article_id = models.ForeignKey(PostArticle, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_notified.username

    class Meta:
        verbose_name = 'notify'
        verbose_name_plural = 'notifies'
