from django.urls import path
from stores import views

urlpatterns = [
    path('list/', views.store_list, name="list"),
]