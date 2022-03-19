from django.urls import path
from uni_fit import views

app_name = 'uni_fit'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('results/', views.review, name='review'),
]
