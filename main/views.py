from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Orders
from .models import Products
from .models import Services
from .forms import OrdersForm


def index(request):
    return render(request, 'main/index.html')


def add_order(request):
    error = ''
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-all-orders')
        else:
            error = 'Форма была не верной'
    form = OrdersForm()
    services = Services.objects.all()
    products = Products.objects.all()
    return render(request, 'main/add_order.html',
                  {'title': 'Добавить заказ', 'services': services, 'products': products, 'forms': form,
                   'error': error})


def edit_order(request, id):
    try:
        order = Orders.objects.get(id=id)
        product = Products.objects.all()
        service = Services.objects.all()
        form = OrdersForm()
        if request.method == "POST":
            order.customers_name = request.POST.get('customers_name')
            order.email = request.POST.get('email')
            order.product = Products.objects.get(id=request.POST.get('product'))
            order.service = Services.objects.get(id=request.POST.get('service'))
            order.save()
            return redirect('show-all-orders')
        else:
            return render(request, 'main/edit.html', {"title": "Редактирование " + str(order.customers_name),
                                                      "order": order, "product": product, "service": service, "form": form})

    except Orders.DoesNotExist:
        return HttpResponseNotFound("<h2>Указанный пользователь не найден</h2>")


def delete_order(request, id):
    order = Orders.objects.get(id=id)
    order.delete()
    return redirect('show-all-orders')


def show_all_orders(request):
    orders = Orders.objects.all()
    return render(request, 'main/show_all_orders.html', {'title': 'Все заказы', 'orders': orders})
