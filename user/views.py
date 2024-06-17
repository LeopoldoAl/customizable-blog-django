from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# it
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render  # , render
from django.views.decorators.csrf import requires_csrf_token
# it
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView  # , TemplateView, DeleteView, DetailView
# from user.models import Profile
# it
from .forms import LoginForm, SignUpForm, PasswordChangingForm, ProfileForm, UserForm  # , UserForm, ProfileForm
# it
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers
from .models import Profile
from my_blog.models import PostArticle, CustomizeBlog
from django.contrib.auth import get_user_model

User = get_user_model()
fromcame = 'index'  # It's from where came
fromcame2 = 'index'  # It's from where came


# from django.shortcuts import render

# from django.contrib.auth import get_user_model

# User = get_user_model()


# from manage_post.models import Article


# Create your views here.

@requires_csrf_token
def dologin(request):
    """
        This function allows me to do login and start session, and then it returns me
        to the page from where I press the login button.
    """
    global fromcame
    if request.method == "GET":
        # My setting
        setting = CustomizeBlog.objects.get(active_setting=True) if len(CustomizeBlog.objects.filter(active_setting=True))==1 else CustomizeBlog.objects.filter(active_setting=True)

        # If the user is authenticated then we lead to the index page
        if request.user.is_authenticated:
            return redirect('index')

        # We take the url from where the user comes
        fromcame = str(request.META.get('HTTP_REFERER'))

        # If the user comes to outside our website the request.META.get('HTTP_REFERER') is None
        # then we lead to the index page

        if request.META.get('HTTP_REFERER') is None:
            fromcame = 'index'

        # We take the user form for login and send it to the login template
        form_class = LoginForm
        return render(request, 'login/login.html', {'form': form_class, 'setting': setting })
    else:
        # We get the user data.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # usertook returns 1 if the user exists but zero if it's not exists
        usertook = len(User.objects.filter(username=username))
        if usertook != 0:
            userpwd = User.objects.filter(username=username).get()
            if not check_password(password, userpwd.password):
                msg = "Your password is not correct!"
                form_class = LoginForm
                # My setting
                setting = CustomizeBlog.objects.get(active_setting=True) if len(CustomizeBlog.objects.filter(active_setting=True))==1 else CustomizeBlog.objects.filter(active_setting=True)
                return render(request, 'login/login.html', {'form': form_class, 'msg': msg,'setting': setting })
        else:
            # My setting
            setting = CustomizeBlog.objects.get(active_setting=True) if len(CustomizeBlog.objects.filter(active_setting=True)) == 1 else CustomizeBlog.objects.filter(active_setting=True)
            msg = "You still aren't registered"
            form_class = LoginForm
            return render(request, 'login/login.html', {'form': form_class, 'msg': msg,'setting': setting, })

        # Get username and password
        user = authenticate(
            username=username,
            password=password,
        )
        if fromcame.find("user/reset/done"):
            fromcame = 'index'
        # Requested of session start
        login(request, user)
        return redirect(fromcame)


@requires_csrf_token
def signup(request):
    global fromcame2
    if request.method == "GET":
        # My setting
        setting = CustomizeBlog.objects.get(active_setting=True) if len(CustomizeBlog.objects.filter(active_setting=True))==1 else CustomizeBlog.objects.filter(active_setting=True)

        # I the user is authenticated then we lead to the index page
        if request.user.is_authenticated:
            return redirect('index')

        # We take the url from where the user comes
        fromcame2 = str(request.META.get('HTTP_REFERER'))

        # If the user comes to outside our website the request.META.get('HTTP_REFERER') is None
        # then we lead to the index page

        if request.META.get('HTTP_REFERER') is None:
            fromcame2 = 'index'

        # We take the user form for login and send it to the login template
        form_class = SignUpForm
        return render(request, 'login/register.html', {'form': form_class, 'setting': setting})
    else:

        # We check if the user exist.
        username = request.POST.get('username')
        # usertook returns 1 if the user exists but zero if it's not exists
        usertook = len(User.objects.filter(username=username))

        if usertook != 0:
            msg = "This user name already exists, please select other user name."
            form_class = SignUpForm
            return render(request, 'login/register.html', {'msg': msg, 'form': form_class, })
        # Get the data from SignUpForm form

        # make_password encripts our password
        password1 = make_password(request.POST.get('password1'))
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_address = request.POST.get('email')

        # We insert the user data in PostArticle
        u = User(
            username=username,
            password=password1,
            first_name=first_name,
            last_name=last_name,
            email=email_address
        )
        # We save the user data
        u.save()

        # Get username and password
        user = authenticate(
            username=username,
            password=request.POST.get('password1'),
        )

        # Requested of session start
        login(request, user)
        return redirect(fromcame2)


@requires_csrf_token
def remove_user(request):
    """ We remove the actual user """
    if request.method == 'GET':
        # My setting
        setting = CustomizeBlog.objects.get(active_setting=True) if len(CustomizeBlog.objects.filter(active_setting=True)) == 1 else CustomizeBlog.objects.filter(active_setting=True)
        msg = 'Do you really wish to delete your account?'
        return render(request, 'profile/delete_user.html', {"msg": msg,'setting': setting, })
    if request.method == 'POST':
        username = request.user.username

        numberuserdelete = User.objects.filter(username=username).get().delete()
        if numberuserdelete[0] > 0:
            """
            print(numberuserdelete[0])
            print(numberuserdelete[1]['auth.User'])
            print(numberuserdelete[1]['user.Profile'])
            """
            return redirect('index')
        else:
            msguser = f" The user {username} could not be deleted, please come back to try it"
            # My setting
            setting = CustomizeBlog.objects.get(active_setting=True) if len(CustomizeBlog.objects.filter(active_setting=True)) == 1 else CustomizeBlog.objects.filter(active_setting=True)
            return render(request, 'profile/delete_user.html', {'msguser': msguser,'setting':setting, })


class PasswordsChangeView(LoginRequiredMixin, PasswordChangeView):
    # We wear the user to session log in form
    login_url = 'login'
    # We change the password inside the following template
    template_name = 'pwd/password_change.html'
    # We place the form that we will use.
    form_class = PasswordChangingForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # My setting
        context['setting'] = CustomizeBlog.objects.get(active_setting=True) if len(CustomizeBlog.objects.filter(active_setting=True))==1 else CustomizeBlog.objects.filter(active_setting=True)
        return context
    # We redirect to the user to the main page
    success_url = reverse_lazy('index')


class UserUpdateView(LoginRequiredMixin, TemplateView):
    # If a person wants to edit your profile should first logging in session
    login_url = 'login'
    user_from = UserForm
    profile_form = ProfileForm

    def post(self, request):

        # Now we go to verify if has ben added a file or if a post request to the from has occurred
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        # And if the data both of user form as profile form are valid I want to save those data
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            # And finally I want to wear them to index page.
            return redirect('index')

        # As in this case we go to send two forms to a template we go using the get_context_data
        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form,
            setting=CustomizeBlog.objects.get(active_setting=True) if len(CustomizeBlog.objects.filter(active_setting=True))==1 else CustomizeBlog.objects.filter(active_setting=True)  # My setting
        )

        return render(request, 'profile/edit_profile.html', context)

    # We create profile if not exists.
    def get(self, request, *args, **kwargs):
        if Profile.objects.filter(user=request.user).exists() == False:
            Profile.objects.create(user=request.user)
        return self.post(request, *args, **kwargs)


class ViewProfile(DetailView):
    model = User
    template_name = 'profile/view_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # My setting
        context['setting'] = CustomizeBlog.objects.get(active_setting=True) if len(CustomizeBlog.objects.filter(active_setting=True))==1 else CustomizeBlog.objects.filter(active_setting=True)
        context['posts'] = PostArticle.objects.filter(user_id=User.objects.get(id=self.kwargs['pk']))
        return context


def senddata(request):
    q = str(request.GET['q']).strip()
    info = ""
    if len(q) > 0:
        q = str(q).lower()
        info = serializers.serialize('json', PostArticle.objects.filter(slug__contains=q))

        return HttpResponse(info,content_type='application/json')
    else:
        info = serializers.serialize('json', info)
        return HttpResponse(info,content_type='application/json')