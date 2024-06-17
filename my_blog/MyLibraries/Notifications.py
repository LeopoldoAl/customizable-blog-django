from my_blog.models import CustomizeBlog

my_update = dict()


def control_main(request, *data):
    """
        data: is a tuple
        data[0] = User
        data[1] = Profile
        data[2] = PostArticle
        data[3] = Rating
        data[4] = Reply
        data[5] = Notification
        data[6] = Notify
        data[7] = kwargs with the slug
        data[8] = Message in the notification
        data[9] = datetime
    """
    # This variable is used for send the data to update in the different model o table
    global my_update

    # We instantiate the "Notifications" class to access to its different methods
    notifying = Notifications(request, data[5])

    comments = data[3].objects.filter(article_id=data[2].objects.get(slug=data[7]['slug'])).exclude(
        user_id=data[0].objects.get(username=request.user.username)).values('user_id').distinct()
    replies = data[4].objects.filter(article_id=data[2].objects.get(slug=data[7]['slug'])).exclude(
        user_id=data[0].objects.get(username=request.user.username)).values('user_id').distinct()

    my_comments = {}
    my_replies = {}
    my_comments = {i['user_id'] for i in comments if not i['user_id'] in my_comments}
    my_replies = {i['user_id'] for i in replies if not i['user_id'] in my_replies}

    comment_in_union_to_comment = my_comments.union(my_replies)

    # We only notify the user that that wrote the article.
    user_wrote_article_name = data[2].objects.get(slug=data[7]['slug']).user_id

    if len(data[5].objects.filter(user=user_wrote_article_name)) > 0:
        my_update = {'has_notifications': True}
        notifying.update_mine(user=user_wrote_article_name)
        print(f"An author notification has been updated successfully!")
    else:
        notifying.insert(user=data[0].objects.get(username=user_wrote_article_name), has_notifications=True)
        print(f"An author notification has been created successfully!")

    """
        We notify all of the users that have commented except the person 
        that wrote the article.
    """
    for i in comment_in_union_to_comment:
        if len(data[5].objects.filter(user=i)) > 0:
            my_update = {'has_notifications': True}
            notifying.update_mine(user=i)
            print(f"The notification has been updated successfully!")
        else:
            notifying.insert(user=data[0].objects.get(id=i), has_notifications=True)
            print(f"The notification has been created successfully!")

    """
            We put the notification message to all of the users that have commented 
            except the person that wrote the article.
    """
    notifying = Notifications(request, data[6])

    # We check if the user that have commented to have profile
    exist_profile_user_commenting = len(data[1].objects.filter(user=data[0].objects.get(id=request.user.id)))

    exist = False

    if exist_profile_user_commenting == 1:
        exist = False if data[1].objects.get(user=data[0].objects.get(id=request.user.id)).photo is None else True

    msg1 = f"1 person did a comment in your article "
    msg2 = f"{len(comment_in_union_to_comment) + 1} people have commented your article "

    if len(data[6].objects.filter(user_notified=user_wrote_article_name,
                                  user_that_commented='Author')) > 0:
        if len(data[6].objects.filter(user_notified=user_wrote_article_name,
                                      data_of_message__contains=msg2)) == 0:
            my_update = {'data_of_message': msg2, 'status_notification': True, }
            notifying.update_mine(user_notified=user_wrote_article_name, user_that_commented='Author')
            print(f"An author notification has been updated and delivered successfully!")
    else:
        notifying.insert(
            slug_image_user_that_commented=CustomizeBlog.objects.get(
                active_setting=True).notification_image.url if len(
                CustomizeBlog.objects.filter(active_setting=True)) else 'static/IMG/notifications.png',
            data_of_message=msg1 if len(comment_in_union_to_comment) == 0 else msg2,
            user_that_commented='Author',
            user_notified=data[0].objects.get(id=data[0].objects.get(username=user_wrote_article_name).id),
            count_notification=1,
            status_notification=True,
            article_id=data[2].objects.get(slug=data[7]['slug']),
        )
        print(f"An author notification has been created and delivered!")

    for u in comment_in_union_to_comment:
        notifying.insert(
            slug_image_user_that_commented=request.user.profile.photo.url if exist else CustomizeBlog.objects.get(
                active_setting=True).profile_default_image.url if exist_profile_user_commenting == 1 else 'static/IMG/profile.png',
            data_of_message=f"<span class='name'>{request.user.first_name}</span> {data[8]} in",
            user_that_commented=request.user.username,
            user_notified=data[0].objects.get(id=u),
            count_notification=1,
            status_notification=True,
            article_id=data[2].objects.get(slug=data[7]['slug']),
        )
        print(f"The notification has been created and delivered!")


class Notifications:
    """
        It only accepts the name of a table and the request
        and the kwargs as a slug like this.
        Example:
         notify = Notifications(request, Profile, id='1', slug='mom',...)
     """

    def __init__(self, request, table, **kwargs):
        self.request = request
        self.table = table
        self.kwargs = kwargs

    def insert(self, **kwargstwo):
        """
                It only accepts the name of the field from the table
                defined as self.table
                Example:
                 fields = notify.insert(id='1', photo='una', ....)
                 or
                 fields = Notifications(request, Profile,slug='mom').insert(id='1', mama='bien',...)
             """
        self.table(**kwargstwo).save()
        return 'operation successful!'

    def update_mine(self, **where):
        """
        It updates the data that bring the updation function
        inside the table that comes in the self.table variable.
        Example:
            notify = Notifications(request, Profile)
            update = notify.updating(slug='amsn', mom='nothing',...)
            update_table = notify.update_mine(id='2', name='jose')
        """
        self.table.objects.filter(**where).update(**my_update)
        my_update.clear()
        return f"{self.table} has been updated with success!"

# fields = Notifications(request, Profile,slug='mom').insert(id='1', mama='bien')
