"""spotipi_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from tags.views import TagCreate, TagUpdate, TagDelete,  TagList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TagList.as_view(), name='tag-list'),
    path('tag/add/', TagCreate.as_view(), name='tag-add'),
    path('tag/<int:pk>/', TagUpdate.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', TagDelete.as_view(), name='tag-delete'),
]
