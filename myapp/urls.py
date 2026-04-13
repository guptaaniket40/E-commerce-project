from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductAPI.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),

    path('cart/create/', CreateCart.as_view()),
    path('cart/add/', AddToCart.as_view()),
    path('cart/<int:cart_id>/', ViewCart.as_view()),
    path('cart/remove/<int:item_id>/', RemoveFromCart.as_view()),

    path('checkout/', Checkout.as_view()),
]