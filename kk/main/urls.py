from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aricels/<slug:slug>',views.specificCategory,name='specific'),
    path('help/',views.help,name ='help'),
    path('new',views.new_topic,name='new')
    ]