from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created

# Create your views here.

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {
        'order':order,
    }
    return render(request, 'admin/orders/order/detail.html', context)

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quentity=item['quentity']
                )
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            context = {
                'order':order,
                }

            return render(request, 'orders/order/created.html', context)

    else:
        form = OrderCreateForm()
    context = {
        'cart':cart,
        'form':form,
        }

    return render(request, 'orders/order/checkout.html', context)