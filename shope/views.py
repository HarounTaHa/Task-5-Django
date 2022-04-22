from django.shortcuts import render
from django.db.models import Q
from .models import Order


# Create your views here.
def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    if q:
        orders_search = Order.objects.filter(
            Q(customer__first_name__icontains=q) | Q(tracking_number__icontains=q) | Q(order_number__icontains=q)
        )
        if orders_search:
            return render(request, 'shope/index.html', context={'orders': orders_search})

    orders = Order.objects.all()
    return render(request, 'shope/index.html', context={'orders': orders})
