from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm, EditUserProfileForm
from django.contrib import messages  
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.

def signup(request):
	if request.method == "POST":
		fm = SignupForm(request.POST)
		if fm.is_valid():
			messages.success(request, 'Account created successfully !!' )
			fm.save()

	else:
		fm = SignupForm()
	return render (request,'enroll/signup.html',{'fm': fm})

def user_login(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			fm = AuthenticationForm(request=request, data = request.POST)
			if fm.is_valid():
				uname = fm.cleaned_data['username']
				upass = fm.cleaned_data['password']
				user = authenticate(username=uname, password=upass)
				if user is not None:
					login(request,user)
					messages.success(request,'Login success')
					return HttpResponseRedirect('/profile/')
		else:
			fm = AuthenticationForm()
		return render(request,'enroll/userlogin.html',{'fm': fm})
	else:
		return HttpResponseRedirect('/profile/')


def user_profile(request):
	#UserChangeForm is imported in forms.py to render a by default form that displays the all the details of User  and We can edit it
	if request.user.is_authenticated:
		if request.method =="POST":
			fm = EditUserProfileForm(request.POST,instance=request.user)
			if fm.is_valid:
				fm.save()
				messages.success(request,'profile updated !!!')

		else:
			fm = EditUserProfileForm(instance=request.user)
		return render(request,'enroll/profile.html',{'name': request.user,'fm':fm})
	else:
		return HttpResponseRedirect('/login/')





def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/login/')

#change password with old password
def user_change_pass(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			fm = PasswordChangeForm(user=request.user, data = request.POST)
			if fm.is_valid():
				fm.save()
				#return HttpResponseRedirect('/profile/') 
				'''when password is changed it must be redirected to profile 
				   but instead it redirects to login page by default, so we should 
				   update our session so that it is redirected to our desired page '''
				update_session_auth_hash(request, fm.user)
				return HttpResponseRedirect('/profile/') 
		else:
			fm = PasswordChangeForm(user=request.user)
		return render(request,'enroll/changepass.html',{'fm': fm})
	else:
		return HttpResponseRedirect('/login')


