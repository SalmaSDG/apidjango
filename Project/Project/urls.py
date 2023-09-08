"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from apicrud import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('login/', views.connexion, name="login"),
    path('register/', views.register, name="register"),
    path('deconnexion/', views.deconnexion, name="logout"),
    path('utilisateur/', views.voirUser, name="voiruser"),
    path('data/',views.showData, name="showData"),
    path('accounts/login/', views.connexion, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logou'),
    path('apicrud/', include('apicrud.urls'),)
]

endpoint = 'http://127.0.0.1:8000/apicrud/emp'