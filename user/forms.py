from django import forms
# it
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from .models import Profile

# from user.models import Profile

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(help_text=None,
                               label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'User name'}))
    password = forms.CharField(label=False,
                               help_text=None,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]


class SignUpForm(UserCreationForm):
    username = forms.CharField(help_text=None,
                               label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'User name'}))
    first_name = forms.CharField(help_text=None,
                                 label=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(help_text=None,
                                label=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.CharField(label=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


# Views for changing user password
class PasswordChangingForm(PasswordChangeForm):
    # We define our model
    model = User

    # We define the attributes for our form
    old_password = forms.CharField(label=False,
                                   widget=forms.PasswordInput(attrs={'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(label=False,
                                    widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}))
    new_password2 = forms.CharField(label=False,
                                    widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    # We put the fields for our form
    fields = [
        'old_password',
        'new_password1',
        'new_password2',
    ]


class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(label=False,
                             help_text=None,
                             required=True,
                             widget=forms.FileInput())

    profession = forms.CharField(label=False,
                                 help_text=None,
                                 required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'Profession'})
                                 )
    about = forms.CharField(label=False,
                            help_text=None,
                            required=False, widget=forms.Textarea(attrs={'placeholder': 'About'}))
    birthday = forms.DateTimeField(label=False,
                                   help_text=None,
                                   required=False, input_formats=None,
                                   widget=forms.TextInput(
                                       attrs={'type': 'date', 'class': '-webkit-calendar-picker-indicator'}))
    twitter = forms.URLField(label=False,
                             help_text=None,
                             required=False,
                             widget=forms.TextInput(attrs={'placeholder': "Twitter's link"}))
    linkedin = forms.URLField(label=False,
                              help_text=None,
                              required=False,
                              widget=forms.TextInput(attrs={'placeholder': "Linkedin's link"}))
    facebook = forms.URLField(label=False,
                              help_text=None,
                              required=False,
                              widget=forms.TextInput(attrs={'placeholder': "Facebook's link"}))

    class Meta:
        model = Profile
        fields = [
            'photo',
            'profession',
            'about',
            'birthday',
            'twitter',
            'linkedin',
            'facebook',
        ]


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text=None,
                               label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'User name'}))

    first_name = forms.CharField(help_text=None,
                                 label=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'First name'}))

    last_name = forms.CharField(help_text=None,
                                label=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Last name'}))

    email = forms.CharField(help_text=None,
                            label=False,
                            widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


"""





"""
