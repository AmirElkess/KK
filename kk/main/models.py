from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User


class Topic(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')
    Title = models.CharField(max_length=200)
    Body = models.TextField()
    positiveVotes = models.IntegerField(default=0)
    negativeVotes = models.IntegerField(default=0)
    # videoLink = models.URLField(max_length=400)
    Category = models.CharField(
        max_length = 3,
        choices = ( ("phy", "Physics"),
                    ("che", "Chemistry"),
                    ("bio", "Biology"),
                    ("eng", "English"),
                    ("ara", "Arabic"),
                    ("his", "History"),
                    ("art", "Arts"),
                    ("ict", "Computer science"),
                    ("mth", "Maths"),
                    ("gen", "General"),
                    ),
        default = "gen",
    )
    timeStamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.Title 

class Comment(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    onArticle = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comments')
    Body = models.CharField(max_length=400)
    timeStamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.Body