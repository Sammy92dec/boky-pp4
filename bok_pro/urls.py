from django.contrib import admin
from django.urls import path, include
from about_app import views as about_views
from booking_app import views as booking_views
from django.contrib.auth import views as auth_views
from .import views 

urlpatterns = [
    path('about/', about_views.about, name='about'), # Routes to about_app
    path('', views.home, name='home'), # Routes to home
    path('booking/', include('booking_app.urls')), # Routes to booking table/reservatons
    path("accounts/", include("allauth.urls")),  # Allauth Authentication
    path('summernote/', include('django_summernote.urls')),    
    path('menu/', include('food_drink.urls')), # Routes to menus
    path('event/', include('events.urls')), # Routes to event posts
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]


