from django.urls import path
from django.contrib.auth.views import login,logout
from category import views

urlpatterns=[
    path('login/',login,{'template_name':'category/login.html'},name='login'),
    path('register/',views.register,name='register'),
    path('query/',views.query,name='query')
]