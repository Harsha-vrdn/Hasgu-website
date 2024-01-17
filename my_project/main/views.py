from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from cart.models import CartItem


@login_required(
    login_url="login"
)  # Redirect to the login page if the user is not logged in
def main(request):
    if request.method == "POST":
        makename = request.POST["makename"]
        url = "https://urban-dictionary7.p.rapidapi.com/v0/define"

        querystring = {"term": makename}

        headers = {
            "X-RapidAPI-Key": "fefc21a094msh1772a23b92d64bbp179dd6jsnc8a9a040ab52",
            "X-RapidAPI-Host": "urban-dictionary7.p.rapidapi.com",
        }

        response = requests.get(url, headers=headers, params=querystring)

        res = [i["definition"] for i in response.json()["list"]]

        # Modify the product_name and price based on your requirements
        product_name = res[0] if res else "Default Product"
        price = 10.00  # Modify this based on the actual price

        # Add the item to the cart
        CartItem.objects.create(
            user=request.user, product_name=product_name, price=price
        )

        return render(request, "main.html", {"res": res})
    return render(request, "main.html")
