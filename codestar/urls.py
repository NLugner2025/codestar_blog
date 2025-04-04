"""
URL configuration for codestar project.

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
from blog import views as blog_views
from django.urls import path
from todos import views

urlpatterns = [
    path('notifications/read/', views.mark_notifications_as_read, name='mark_notifications_as_read'),
    path("blog/", blog_views.my_blog, name='blog'),
    path('admin/', admin.site.urls),
    # …
    path("accounts/", include("allauth.urls")),
    # …
    path('', views.ListTodo.as_view(), name='list-todo'),
    path('todos/create/', views.CreateTodo.as_view(), name='create-todo'),
    path('todos/update/<int:pk>', views.UpdateTodo.as_view(), name='update-todo'),
    path('todos/delete/<int:pk>', views.DeleteTodo.as_view(), name='delete-todo'),
]
