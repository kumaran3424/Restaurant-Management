"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app1.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('menu-details',menu_details,name='menu_details'),
    path('menu-list',menu_list,name='menu_list'),
    path('category_list',category_list,name='category-list'),
    path('chef-list',chef_list,name='chef_list'),
    path('add-menu-item',add_menu_item,name='add-menu'),
    path('add-chef',add_new_chef,name='chef_add'),
    path('directions' , maps,name="directions")
    
]