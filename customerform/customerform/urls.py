"""customerform URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import path
from form import views as form_views
from users import views as UserViews
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),

    #Form App Url's
    path('BlogPost/', form_views.BlogPost,name='BlogPost'),
    path('BlogPostClass/', form_views.BlogPostClass.as_view(),name='BlogPostClass'),

    path('BlogView/', form_views.BlogView,name='BlogView'),
    path('BlogDetailView/<id>', form_views.BlogDetailView,name='BlogDetailView'),

    path('BlogUpdateView/<id>', form_views.BlogUpdateView,name='BlogUpdateView'),
    path('BlogUpdateClass/<pk>', form_views.BlogUpdateClass.as_view(),name='BlogUpdateClass'),

    #Users App Url's
    path('Registration/', UserViews.Registration,name='Registration'),
    path('Profile/', UserViews.Profile,name='Profile'),
    path('Login/', auth_views.LoginView.as_view(template_name='users/Login.html'),name='Login'),
    path('Logout/', auth_views.LogoutView.as_view(template_name='users/Logout.html'),name='Logout'),
   
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)