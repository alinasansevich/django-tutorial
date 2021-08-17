"""mysite URL Configuration

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
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('polls.urls')),
    path('polls/', include('polls.urls')),
]


# the line I added raised this warning:
# WARNINGS:
# ?: (urls.W005) URL namespace 'polls' isn't unique. You may not be able to reverse all URLs in this namespace
 
# https://stackoverflow.com/questions/53473027/django-warning-urls-w005-url-namespace-isnt-unique