"""DatabaseCaching URL Configuration

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
from enroll import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    #creating cache for url that use same view as below 
    path('contactcache/',cache_page(60)(views.contact)),
    path('contact/',views.contact),
]
'''  Here we created 2 urls that hits views.contact
where contactcache url uses caching for 60 seconds and contact url don't '''
