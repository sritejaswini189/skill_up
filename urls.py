from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('courses/', views.courses, name='courses'),
    path('branch/', views.branch, name='branch'),
    path('cse/',views.cse, name='cse'),
    path('ece/',views.ece, name='ece'),
    path('java/',views.java, name='java'),
    path('python/',views.python, name='python'),
    path('html_css/',views.html_css, name='html_css'),
    path('analog/',views.analog, name='analog'),
    path('control/',views.control, name='control'),
]
