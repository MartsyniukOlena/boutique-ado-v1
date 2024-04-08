from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51P3FR6HC3w24nuCvMtGI0aH78RyQdjC1uqeSXwW4O2zmmQH22rkvLZjtEkeDWpPjnfXy8hZWAvWyfI666hucheQM00b5kZ2Fft',
        'client_secret': 'test client key',
    }

    return render(request, template, context)