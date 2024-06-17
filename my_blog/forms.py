from django import forms
from my_blog.models import Rating, Reply


class Comment(forms.ModelForm):
    comment = forms.CharField(required=False,
                              widget=forms.Textarea(
                                  attrs={'rows': 5, 'maxlength': 255, 'placeholder': 'Write your commentaries here.'}))

    value = forms.CharField(help_text=None,
                            label=False,
                            widget=forms.TextInput(attrs={'value': 0, 'type': 'hidden', 'placeholder': 'Nothing'}))

    class Meta:
        model = Rating
        fields = [
            'comment',
            'value',
        ]
