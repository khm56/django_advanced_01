from django.urls import path
from inventories import views

urlpatterns = [
    path('list/', views.inventory_list, name="list"),
]