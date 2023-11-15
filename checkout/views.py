from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Theres nothing in your bag at the moment')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51OCqypBdKna3LSPr9mkDk2sQO9VS4DiQlFsWchNXRfVSYxEUteVrYrwD9uHg0a5puGwgnLYuzmaq3N64jxJzXGux00U63GNTA9',
        "client_secret": 'test_client_secret'
    }
    return render(request, template, context)
