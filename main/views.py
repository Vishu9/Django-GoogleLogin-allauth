
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

def homepage(request):
	return render(request, 'home.html')

# def register(request):
# 	if request.method == "POST":
# 		form = UserCreationForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			username = form.cleaned_data.get('username')
# 			messages.success(request, f"New account created: {username}")
# 			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
# 		else:
# 			messages.error(request,"Account creation failed")

# 		return redirect("main:home")

# 	form = UserCreationForm()
# 	return render(request,"register.html", {"form": form})


