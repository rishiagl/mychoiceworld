"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
# from oauth2_provider import urls as oauth2_urls


urlpatterns = [
    path("", views.index, name="index"),
    # path('o/', include(oauth2_urls)),
    path("__reload__/", include("django_browser_reload.urls")),
    path('marketing/', include("marketing.urls")),
    path('catalog/', include("catalog.urls")),
    path('flipkart/', include("flipkart.urls")),
    path('retail/', include("retail.urls")),
    path('admin/', admin.site.urls),
]
