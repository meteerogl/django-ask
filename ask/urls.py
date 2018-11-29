"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url,include
from accounts.views import register_view
from accounts.views import login_view
from accounts.views import user_view
from django.conf.urls.static import static
from django.conf import settings

from accounts.views import Register
from accounts.views import Restlogin




urlpatterns = [
    url('admin/', admin.site.urls),
    url(r"^$",view=login_view),
    url(r"^login/$",view=login_view,name="login"),
    url(r"^register/$",view=register_view,name="register"),
    url(r"^accounts/",include("accounts.urls")),
    #REST API ICIN OLANLAR
    #------
    url(r"^restregister/$",view=Register.as_view(),name="restregister"),
    url(r"^restlogin/$",view=Restlogin.as_view(),name="restlogin"),
    #------
    url(r"^(?P<username>[-\w]+)/$",view=user_view,name="user-view"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
