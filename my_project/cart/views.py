from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError, HttpResponseNotFound
from .models import CartItem


@login_required(login_url="login")
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.price for item in cart_items)
    return render(
        request,
        "cart/view_cart.html",
        {"cart_items": cart_items, "total_price": total_price},
    )


@login_required(login_url="login")
def add_to_cart(request, product_name, price):
    try:
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user, product_name=product_name, price=price
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect("view_cart")
    except Exception as e:
        return HttpResponseServerError("An error occurred while adding to the cart.")


@login_required(login_url="login")
def remove_from_cart(request, cart_item_id):
    try:
        cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
        cart_item.delete()
        return redirect("view_cart")
    except Http404:
        return HttpResponseNotFound("Cart item not found.")
    except Exception as e:
        return HttpResponseServerError(
            "An error occurred while removing from the cart."
        )
