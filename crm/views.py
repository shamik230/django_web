from django.shortcuts import render
from .models import Order

# Create your views here.


def index(request):
    order_list = Order.objects.all()
    data = {"order_list": order_list}
    return render(request, "index.html", data)


def thanks(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, 'thanks.html')

