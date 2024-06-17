# For drive queries we use
# https://docs.djangoproject.com/en/4.2/topics/db/queries/
# https://docs.djangoproject.com/en/4.2/ref/models/querysets/#queryset-api
# https://docs.djangoproject.com/en/4.2/ref/models/expressions/
# For drive redirections we use
# https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/
# https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/
# Woking with csrf_token
# https://docs.djangoproject.com/en/4.2/howto/csrf/#using-csrf
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.contrib.auth import get_user_model
from my_blog.models import PostArticle, Rating, Reply, Notify, CustomizeBlog
from user.models import Profile, Notification
from my_blog.forms import Comment
#from django.db.models import Count, F
import json
from my_blog.MyLibraries.ManageComments import Commentaries
from my_blog.MyLibraries.Notifications import control_main
from my_blog.MyLibraries.PredictableSearch import fetch_data_to_show_in_input_deployed
from datetime import datetime, timezone


User = get_user_model()


# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {'mano': 'Hello world'})

@ensure_csrf_cookie
def show_articles(request):
    """ This function is used for send article details to the index template """
    if request.method == 'GET':
        # My setting
        setting = CustomizeBlog.objects.get(active_setting=True) if len(
            CustomizeBlog.objects.filter(active_setting=True)) == 1 else CustomizeBlog.objects.filter(
            active_setting=True)

        # We lookup for only the 50 articles more recent
        context = PostArticle.objects.order_by("-created").all()[:50]

        # We lookup for only the 10 articles more recent
        bar_lateral = PostArticle.objects.order_by("-created").all()[:10]

        # We check if there are notifications
        notifications = False
        thereIsNotifications = 0
        if request.user.is_authenticated and len(Notification.objects.filter(user_id=request.user.id).all()) > 0:
            notifications = Notification.objects.get(user_id=request.user.id).has_notifications
            thereIsNotifications = len(
                Notify.objects.filter(user_notified=request.user.id, status_notification=True).all())

        # We send the variables context and bar_lateral to our index template
        return render(request, 'pages/index.html', {'mano': 'Hello world', 'articles': context
            , 'barLateral': bar_lateral, 'notifications': notifications,
                                                    'thereIsNotifications': thereIsNotifications,
                                                    'setting': setting})
    else:
        data = json.loads(request.body)
        id = Commentaries(data, None)
        if id.data['id'] == 'search':
            search_brutal = id.data['searching']
            search = str(search_brutal).lower()

            search_title = PostArticle.objects.filter(title__contains=search) or PostArticle.objects.filter(
                title__contains=search_brutal)
            search_description = PostArticle.objects.filter(description__contains=search) or PostArticle.objects.filter(
                description__contains=search_brutal)
            search_body = PostArticle.objects.filter(body__contains=search) or PostArticle.objects.filter(
                body__contains=search_brutal)
            if len(search_title) > (len(search_description) or len(search_body)):
                return render(request, 'pages/search.html',
                              {'articles': search_title, })
            elif len(search_description) > (len(search_title) or len(search_body)):
                return render(request, 'pages/search.html',
                              {'articles': search_description, })
            elif len(search_body) > (len(search_title) or len(search_description)):
                return render(request, 'pages/search.html',
                              {'articles': search_body, })
            else:
                msg = 'Wao, Nothing has found!'
                return render(request, 'messages/search-not-found.html',
                              {'foundresses': msg, })
        if id.data['id'] == 'show_notifications':
            if id.data['indentify'] == 0:
                # We bring all of the notification of the user logged in
                user_data = Notify.objects.filter(user_notified=request.user.id).order_by('-status_notification',
                                                                                          '-created')

                return render(request, 'layout/show-notifications.html',
                              {'user_data': user_data, })
            else:
                # We update 'status_notification' to False
                Notify.objects.filter(user_notified=request.user.id
                                      , status_notification=True).update(status_notification=False)

                # We bring all of the notification of the user logged in
                user_data2 = Notify.objects.filter(user_notified=request.user.id).order_by('-updated')

                return render(request, 'layout/show-notifications.html',
                              {'user_data2': user_data2, })


@ensure_csrf_cookie
def send_articles_body(request, **kwargs):
    """ This function is used for send article details to the index template """
    if request.method == 'GET':
        # My setting
        setting = CustomizeBlog.objects.get(active_setting=True) if len(
            CustomizeBlog.objects.filter(active_setting=True)) == 1 else CustomizeBlog.objects.filter(
            active_setting=True)

        slug = kwargs['slug'].lower()

        # We get the slug from the article atual
        myslug = PostArticle.objects.get(slug=slug)

        # We access to number_of_ping-backs from the actual slug and and we add 1 to this value
        count = int(myslug.number_of_ping_backs) + 1

        # Lastly we asign the new value to the context variable context
        views = count
        show_view = views
        if 1000 <= views < 1000000:
            show_view = str(round(views / 1000, 1)) + "K"
        elif views >= 1000000:
            show_view = str(round(views / 1000000, 1)) + "M"

        # We update the number_of_pingbacks field with the count value
        PostArticle.objects.filter(slug=slug).update(number_of_ping_backs=count)

        # We lookup for only the 50 articles more recent
        context = PostArticle.objects.filter(slug=slug).order_by('-created').get()
        hello = Commentaries('', None)
        context.created = hello.working_date_time(context.created)
        # if show_views==True we show the view inside the bar side
        WeShowViews = PostArticle.objects.get(slug=slug).show_views
        # if show_comment_with_date==True we show the date inside the commentaries
        we_show_comment_with_date = PostArticle.objects.get(slug=slug).show_comment_with_date
        # We lookup for only the 10 articles more recent
        bar_lateral = PostArticle.objects.order_by("-created").all()[:10]
        # We lookup for only the 10 articles more recent
        old_comment = Rating.objects.filter(article_id=PostArticle.objects.filter(slug=kwargs['slug']).get()).order_by(
            "-created").all()

        # We modify the time of publication of a commentary with
        # how much times ago the comment has been written.
        for i in old_comment:
            if we_show_comment_with_date:
                i.created = hello.working_date_time(i.created, 12)
            else:
                i.created = hello.working_date_time(i.created)

        numberComments = int(len(old_comment))
        # We take the name of the user what wrote the article.
        username = User.objects.get(username=myslug.user_id).first_name
        # We take the last name of the user what wrote the article.
        lastname = User.objects.get(username=myslug.user_id).last_name
        # We take the image of the user pofile what wrote the article.
        # We check if Profile has some profile created yet
        if len(Profile.objects.filter(user_id=myslug.user_id)) != 0:
            photo = Profile.objects.get(user_id=myslug.user_id).photo
        else:
            photo = ''

        # We take the id of the user what wrote the article.
        pk = User.objects.get(username=myslug.user_id).id

        comment_form = Comment
        # We send the variables context and bar_lateral to our index template

        # We check if there are notifications
        notifications = False
        thereIsNotifications = 0
        if request.user.is_authenticated and len(Notification.objects.filter(user_id=request.user.id).all()) > 0:
            notifications = Notification.objects.get(user_id=request.user.id).has_notifications
            thereIsNotifications = len(
                Notify.objects.filter(user_notified=request.user.id, status_notification=True).all())
        return render(request, 'post/articles.html',
                      {'articles': context, 'barLateral': bar_lateral,
                       'views': show_view,
                       'WeShowViews': WeShowViews, 'username': username,
                       'lastname': lastname, 'photo': photo,
                       'pk': pk, 'comment_form': comment_form,
                       'old_comment': old_comment,
                       'numberComments': numberComments,
                       'show_date': we_show_comment_with_date,
                       'notifications': notifications,
                       'thereIsNotifications': thereIsNotifications,
                       'setting': setting})
    if request.method == 'POST':
        # How the data doesn't come from a form, we are not use request.POST otherwise we use
        # request.body and parse the data with the library json imported
        data = json.loads(request.body)
        id = Commentaries(data, None)
        # My setting
        setting = CustomizeBlog.objects.get(active_setting=True) if len(
            CustomizeBlog.objects.filter(active_setting=True)) == 1 else CustomizeBlog.objects.filter(
            active_setting=True)
        if id.data['id'] == 'unique':
            if not request.user.is_authenticated:
                msg = 'To comment first should be logged in'
                return HttpResponse(msg)
            # We get the slug field and the user that is commenting
            slug = PostArticle.objects.filter(slug=kwargs['slug']).get()
            user = User.objects.filter(id=request.user.id).get()

            # Let's investigate if the field comment comes with something
            thereis = Commentaries(data, Rating, slug=slug, user=user, date=datetime.today())
            if thereis.data['id'] == 'unique':
                # data = {'success': 'Commentary was success!'}
                exists = thereis.commentexists('comment')
                if exists == '':
                    return HttpResponse('Please, write a comment!')

                # if the value of stars is zero then we put five stars
                thereis.sendingdata()

                # data = {'success': 'Commentary was success!'}
                thereis.working_date_time(thereis.time_comment_recent())

                # Only we present one comment that is the most recent.
                old_comment = Rating.objects.filter(
                    article_id=PostArticle.objects.filter(slug=kwargs['slug']).get()).order_by(
                    "-created").all()[0]
                we_show_comment_with_date = PostArticle.objects.get(slug=kwargs['slug']).show_comment_with_date
                if we_show_comment_with_date:
                    old_comment.created = thereis.working_date_time(old_comment.created, 12)
                else:
                    old_comment.created = thereis.working_date_time(old_comment.created)

                # We notify the user
                control_main(request, User, Profile, PostArticle, Rating, Reply, Notification, Notify, kwargs,
                             'write a new commentary')
                return render(request, 'comment/show-recent-commentaries.html',
                              {'old_comment': old_comment, 'setting': setting, })

        if id.data['id'] == 'showReplies':
            # Only we present one comment that is the most recent.
            thereis = Commentaries(data, Reply)

            # This fetch the data of the users that have responded to one user
            answers = Reply.objects.filter(
                article_id=PostArticle.objects.filter(slug=kwargs['slug']).get(),
                comment_identity=id.data['id_value']).order_by("-created").all()

            # User that has been commented
            user_commented = Rating.objects.filter(
                article_id=PostArticle.objects.filter(slug=kwargs['slug']).get(),
                id=id.data['id_value']).order_by("-created").all()[0]

            we_show_comment_with_date = PostArticle.objects.get(slug=kwargs['slug']).show_comment_with_date
            for i in answers:

                if we_show_comment_with_date:
                    i.created = thereis.working_date_time(i.created, 12)
                else:
                    i.created = thereis.working_date_time(i.created)

            return render(request, 'comment/replies.html',
                          {'answers': answers,
                           'user_commented': user_commented, 'setting': setting, })

        if id.data['id'] == 'search':
            search_brutal = id.data['searching']
            search = str(search_brutal).lower()

            search_title = PostArticle.objects.filter(title__contains=search) or PostArticle.objects.filter(
                title__contains=search_brutal)
            search_description = PostArticle.objects.filter(description__contains=search) or PostArticle.objects.filter(
                description__contains=search_brutal)
            search_body = PostArticle.objects.filter(body__contains=search) or PostArticle.objects.filter(
                body__contains=search_brutal)
            if len(search_title) > (len(search_description) or len(search_body)):
                return render(request, 'pages/search.html',
                              {'articles': search_title, })
            elif len(search_description) > (len(search_title) or len(search_body)):
                return render(request, 'pages/search.html',
                              {'articles': search_description, })
            elif len(search_body) > (len(search_title) or len(search_description)):
                return render(request, 'pages/search.html',
                              {'articles': search_body, })
            else:
                msg = 'Wao, Nothing has found!'
                return render(request, 'messages/search-not-found.html',
                              {'foundresses': msg, })
        if id.data['id'] == 'answers':
            if not request.user.is_authenticated:
                msg = 'To comment first should be logged in'
                return HttpResponse(msg)
            exists = id.commentexists('reply')
            if exists == '':
                msg = 'Please, write a reply'
                return HttpResponse(msg)

            slug = PostArticle.objects.filter(slug=kwargs['slug']).get()
            # user_that_commented = User.objects.filter(first_name=data['first_name'], last_name=data['last_name']).get()
            rating = Rating.objects.get(id=int(data['id_comment']), article_id=slug)
            user = User.objects.filter(id=request.user.id).get()
            user2 = rating
            replies = Commentaries(data, Reply, slug=slug, user2=user2, user=user,
                                   date=datetime.today())
            one_new_reply = replies.sendingdatareply()
            if one_new_reply == 1:
                number_of_reply_actual = int(rating.number_of_reply)
                number_of_reply_new = number_of_reply_actual + 1
                Rating.objects.filter(id=int(data['id_comment']), article_id=slug).update(
                    number_of_reply=number_of_reply_new)
            # We notify the user
            control_main(request, User, Profile, PostArticle, Rating, Reply, Notification, Notify, kwargs,
                         'has wrote a reply')
            return HttpResponse(one_new_reply)

        if id.data['id'] == 'show_notifications':
            if id.data['indentify'] == 0:
                # We bring all of the notification of the user logged in
                user_data = Notify.objects.filter(user_notified=request.user.id).order_by('-created')

                return render(request, 'layout/show-notifications.html',
                              {'user_data': user_data, 'setting': setting, })
            else:
                # We update 'status_notification' to False
                Notify.objects.filter(user_notified=request.user.id
                                      , status_notification=True).update(status_notification=False)

                # We bring all of the notification of the user logged in
                user_data2 = Notify.objects.filter(user_notified=request.user.id).order_by('-created')

                return render(request, 'layout/show-notifications.html',
                              {'user_data': user_data2, 'setting': setting})