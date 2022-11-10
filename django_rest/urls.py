"""django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny, IsAuthenticated

from search_algorithm.routers import routes as search_algorithm_router

router = routers.SimpleRouter()
router.registry.extend(search_algorithm_router.registry)

documentation = include_docs_urls(
    public=True,
    title="Django REST",
    permission_classes=[]
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('docs/', documentation, name="docs"),
    re_path('(^(?!(admin|docs)).*$)', admin.site.urls, name='index'),
]
