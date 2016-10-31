"""Imgr_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from image_gallery.views import UserCreateView, IndexView, ImageListView, ImageCreateView, ImageUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^images$', ImageListView.as_view(), name="image_list_view"),
    url(r'^create/$', ImageCreateView.as_view(), name="image_create_view"),
    url(r'^update/(?P<pk>\d+)/$', ImageUpdateView.as_view(), name="image_update_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
