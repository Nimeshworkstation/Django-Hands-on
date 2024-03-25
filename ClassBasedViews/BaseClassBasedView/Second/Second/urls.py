"""Second URL Configuration

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
    path('homefun/', views.homefunc, name = 'homefunc'),
    path('aboutfun/',views.aboutfunc, name = 'aboutfunc'),
    path('contactfun/',views.contactfunc, name = 'contactfunc'),
    #path('newsfun/',views.newsfunc, name = 'newsfunc'),
    # We will define Two Urls that will use same view function to render two different html Files
    ###########################
    path('newsfun1/',views.newsfunc,{'template_name':'school/news1.html'}, name = 'newsfunc1'),
    path('newsfun2/',views.newsfunc,{'template_name':'school/news2.html'}, name = 'newsfunc2'),
    #################################
    path('homecl/', views.HomeClassView.as_view(), name = 'homeclass'),
    path('aboutcl/', views.AboutClassView.as_view(), name = 'aboutclass'),
    path('contactcl/', views.ContactClassView.as_view(), name = 'contactclass'),

    #path('newscl/', views.NewsClassView.as_view(), name = 'Newsclass'),
    ###############################################
    #We will define two Urls that will use same view class to render tow different html
    path('newscl1/', views.NewsClassView.as_view(template_name = 'school/news1.html'), name = 'Newsclass1'),
    path('newscl2/', views.NewsClassView.as_view(template_name = 'school/news2.html'), name = 'Newsclass2'),



]
