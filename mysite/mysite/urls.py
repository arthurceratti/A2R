"""mysite URL Configuration

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
from django.urls import include, path
from myapp import views as myapp_views
from register import views as register_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/', myapp_views.detail, name='detail'), #observar que detail é importado de myapp/views.py "as" myapp_views.detail (_____."função dentro de views")
    path('', myapp_views.index, name='index'),#observar que detail é importado de myapp/views.py "as" myapp_views.detail (_____."função dentro de views")
    #path('accounts/', include('allauth.urls')),
    path('login/empresa/create/', myapp_views.create, name='create'),#observar que detail é importado de myapp/views.py "as" myapp_views.detail (_____."função dentro de views")
    path('',include("django.contrib.auth.urls")),
    path('register/', register_views.register, name="register" ),
    ] 

