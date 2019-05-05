from django import forms
from .models import Topic
CHOICES = ( ("phy", "Physics"),
                    ("che", "Chemistry"),
                    ("bio", "Biology"),
                    ("eng", "English"),
                    ("ara", "Arabic"),
                    ("his", "History"),
                    ("art", "Arts"),
                    ("ict", "Computer science"),
                    ("mth", "Maths"),
                    ("gen", "General"),
                    )

# Fields that are not sepcifi

class NewTopicForm(forms.ModelForm):
    Body = forms.CharField(widget=forms.Textarea(), max_length=40000)
    message = forms.CharField(widget=forms.Textarea(), max_length=4000)
    # Category = forms.CharField(widget=forms.Select(choices=CHOICES))

    class Meta:
        model = Topic
        fields = ['Title', 'Body','Category','positiveVotes','message']