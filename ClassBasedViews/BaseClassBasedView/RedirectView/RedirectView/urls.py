"""RedirectView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #using template view
    path('',views.TemplateView.as_view(template_name='school/home.html'), name  = 'blankhome'),
    #using Redirect view to redirect home/ to root and also changing url , not home/ but root
    path('home/', views.RedirectView.as_view(url = '/'), name = 'home'),
    #Redirecting to external Link
    path('utube/',views.RedirectView.as_view(url = 'https://www.youtube.com'), name = 'youtube'),
    #Redirecting to external link by defining in view
    path('utube/',views.YoutubeRedirectView.as_view(url = 'https://www.youtube.com'), name = 'youtube'),
    #using pattern name of home to redirect index/ to home/ and from home it is redirected to /
    path('index/', views.RedirectView.as_view(pattern_name = 'home'), name = 'index'),
   #using integer
    path('home/<int:pk>/',views.YouRedirectView.as_view(), name = 'youtube'),
    path('<int:pk>/',views.TemplateView.as_view(template_name = 'school/home.html'), name = 'mhome'),
    #using slug
   # path('home/<slug:post>/',views.YouRedirectView.as_view(), name = 'youtube'),
    #path('<slug:post>/',views.TemplateView.as_view(template_name = 'school/home.html'), name = 'mhome'),


]

