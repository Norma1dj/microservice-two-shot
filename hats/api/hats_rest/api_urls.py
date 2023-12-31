from django.urls import path
from .api_views import api_list_hat

urlpatterns = [
    path("hats/", api_list_hat, name="api_list_hat"),
    path("hats/<int:pk>/", api_list_hat, name="api_show_hat"),
]
