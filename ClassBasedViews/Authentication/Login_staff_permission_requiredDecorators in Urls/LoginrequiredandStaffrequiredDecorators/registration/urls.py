from django.urls import path
from registration import views
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

urlpatterns = [
#checking for login before accessing profile page
path('profile/',login_required(views.ProfileTemplateView.as_view()), name = 'profile'),
#checking for staff member before accessing about page
path('about/',staff_member_required(views.AboutTemplateView.as_view()), name = 'about'),
]