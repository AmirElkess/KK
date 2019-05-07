from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.land, name='land'),
    path('home', views.home, name='home'),
    path('new',views.new_topic,name = 'new'),
    path('<slug:slug>',views.specificCategory,name='specific'),
    path('<slug:slug>',views.specificCategory,name='specific'),
    path('<slug:slug>/<int:id>', views.specificArticle,name='specificarticel'),
    path('help',views.help,name ='help'),
    ]