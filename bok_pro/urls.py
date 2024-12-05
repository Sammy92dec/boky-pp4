"""
URL configuration for bok_pro project.

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
from about_app import views as about_views
from bok_app import views as home_views
from booking_app import views as booking_views

urlpatterns = [
    path('about/', about_views.about, name='about'), # Routes to about_app
    path('',home_views.home, name='home'), # Routes to bok_app
    path('booking/', booking_views.booking, name='booking'),  # Routes to booking_app
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]


