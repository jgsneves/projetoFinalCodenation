"""projectAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token
from projectAPI.api import views

urlpatterns = [
    #admin routes
    path('admin/', admin.site.urls),

    #users routes
    path('users/', views.get_users, name='users_list'),
    path('users/<int:pk>', views.get_single_user, name='single_user'),
    path('users/register/', views.sign_up_user, name='register_user'),

    #login/auth route
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    #report routes
    path('reports/', views.get_reports, name='reports_list'),
    path('reports/<int:pk>', views.handle_single_report, name='single_report'),
    path('reports/new', views.new_report, name='create_report'),
]
