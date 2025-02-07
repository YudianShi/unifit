from django.urls import path
from uni_fit import views

app_name = 'uni_fit'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('university/',views.reddit, name='reddit'),
    path('fav/<int:id>',views.favourite_add, name='favourite_add'),
    path('favourites/',views.favourite_list, name='favourite_list'),
    path('review/', views.post_detail, name='post_detail')
]