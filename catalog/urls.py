from django.urls import path
from .views import HomeView, ContactsView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
