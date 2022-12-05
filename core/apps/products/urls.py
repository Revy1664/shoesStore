from django.urls import path

from .views import ListBrand, DetailBrand

urlpatterns = [
    path('brands', ListBrand.as_view()),
    path('brands/<str:slug>', DetailBrand.as_view(),)
]