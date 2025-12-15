from django.urls import path
from .views import RestaurantListView, RestaurantCreateView

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/add/', RestaurantCreateView.as_view(), name='restaurant-add'),
]
