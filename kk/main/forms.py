from django import forms
from .models import Topic,Comment
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CHOICES = ( ("gen", "General"),
                    ("che", "Chemistry"),
                    ("bio", "Biology"),
                    ("eng", "English"),
                    ("ara", "Arabic"),
                    ("his", "History"),
                    ("art", "Arts"),
                    ("ict", "Computer science"),
                    ("mth", "Maths"),
                    ("phy", "Physics"),
                    )

# Fields that are not sepcifi

class NewTopicForm(forms.ModelForm):
    Body = forms.CharField(widget=forms.Textarea(), max_length=40000, min_length=500)
    Category = forms.CharField(widget=forms.Select(choices=CHOICES))

    class Meta:
        model = Topic
        fields = ['Title', 'Body','Category','videoLink']



class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['Body']