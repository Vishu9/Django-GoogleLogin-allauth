from django.contrib import admin
from django.urls import path, include
from main import views
 

urlpatterns = [
    #path('', include('main.urls')),
    path('',views.homepage,name='home'),
    path('admin/', admin.site.urls),
    #path("register/", views.register, name="register"),
    path('accounts/', include('allauth.urls')),
    path('/accounts/logout/',include('allauth.urls')),
    path('/accounts/login/',include('allauth.urls')),
]
