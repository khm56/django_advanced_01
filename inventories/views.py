from django.shortcuts import render, redirect
from .models import Inventory

# Create your views here.
def inventory_list(request):
    inventories = Inventory.objects.all()
    query = request.GET.get('q')
    if query:
        inventories = inventories.filter(
            Q(name__icontains=query)|
            Q(store__name__icontains=query)
        ).distinct()

    # favorite_list = []
    # if request.user.is_authenticated:
    #     favorite_list = request.user.favoriterestaurant_set.all().values_list('restaurant', flat=True)

    context = {
       "inventories": inventories,
       # "favorite_list": favorite_list
    }
    return render(request, 'list.html', context) 