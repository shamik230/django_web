from django.shortcuts import render
from .models import Order
from .forms import OrderForm

# Create your views here.


def index(request):
    order_list = Order.objects.all()
    form = OrderForm()
    data = {
        "order_list": order_list,
        "form": form,
    }
    return render(request, "index.html", data)


def thanks(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, 'thanks.html')

