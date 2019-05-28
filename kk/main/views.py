from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Topic,Comment
from django.contrib.auth import login as auth_login
from .forms import NewTopicForm, NewComment
from django.contrib.auth.models import User
from django.contrib.auth import get_user


def new_topic(request):
    user = get_user(request)   # TODO: get the currently logged in user
    print(user)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            Topic = form.save(commit=False)
            Topic.Author = user
            Topic.save()
            return redirect('home')  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'main/newTopic.html', {'form': form})

def home(request):
    topics_list = get_list_or_404(Topic) 
    data = {'topics_list': topics_list}
    return render(request, 'main/home.html',context=data)


def help(request):
    return render(request,'main/help.html')

def specificCategory(request,slug):
    topics_list = get_list_or_404(Topic,Category = slug)
    data = {'topics_list': topics_list}
    return render(request, 'main/home.html',context=data)

def specificArticle(request, slug,id):
    user = get_user(request)  
    cat= slug
    ID = id
    topic = get_object_or_404(Topic,id = id) 
    if( Comment.objects.filter(onArticle = topic)):
        comments =  Comment.objects.filter(onArticle = topic)
    else:
        comments = 'None'
    form = NewComment()
    if request.method == 'POST':
        form = NewComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Author = user
            comment.onArticle = topic
            comment.save()
            return redirect(specificArticle,slug = cat, id = ID)  # TODO: redirect to the created topic page
    return render(request, 'main/single.html',{'topic': topic, 'form':form,'Comments' : comments})


def land(request):
    return render(request, 'main/landing-page.html')
       