from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/<int:id>", views.view_product, name="view_product"),
    path("payment/<int:id>", views.payment, name="payment"),
    path("success", views.payment_success, name="success"),
    path("products", views.products, name="products"),
    path("discounts", views.discounts, name="discounts"),
    path("gift_cards", views.gift_cards, name="gift_cards"),
    path("client_days", views.client_days, name="client_days")
]