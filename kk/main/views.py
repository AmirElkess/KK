from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Topic,Comment
from django.contrib.auth import login as auth_login
from .forms import NewTopicForm, NewComment
from django.contrib.auth.models import User


def new_topic(request):
    user = User.objects.first()  # TODO: get the currently logged in user
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
    user = User.objects.first()  
    cat= slug
    ID = id
    topic = get_object_or_404(Topic,id = id) 
    comments = get_list_or_404(Comment , onArticle = topic)
    form = NewComment()
    if request.method == 'POST':
        form = NewComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Author = user
            comment.onArticle = topic
            comment.save()
            return redirect(specificArticle,slug = cat, id = ID)  # TODO: redirect to the created topic page
    return render(request, 'main/single.html',{'topic': topic, 'form':form, 'Comments':comments})


def land(request):
    return render(request, 'main/landing-page.html')
       