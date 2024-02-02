from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from cart.models import CartItem
from .forms import makeNameForm
from django.contrib import messages

# @login_required(
#     login_url="user_login"
# )  # Redirect to the login page if the user is not logged in

def defList(text):
    url = "https://urban-dictionary7.p.rapidapi.com/v0/define"

    querystring = {"term": text}
    headers = {
        "X-RapidAPI-Key": "fefc21a094msh1772a23b92d64bbp179dd6jsnc8a9a040ab52",
        "X-RapidAPI-Host": "urban-dictionary7.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    return [i["definition"] for i in response.json()["list"]]




def main(request):
    input_text = ""
    res = []
    form = makeNameForm()

    if request.method == "POST":
        form = makeNameForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data["makename"]
            selected_option = request.POST.get("dropdown")
            name = ""
            res = defList(input_text)  # Replace with the correct implementation of defList
            price = 10.00

            if selected_option:
                product_name = (
                    f"{input_text} - {selected_option}" if selected_option else "Default Product"
                )
                if request.POST.get("action") == "AddToCart":
                    # Assuming CartItem model is properly defined
                    CartItem.objects.create(
                        user=request.user, product_name=product_name, price=price
                    )
                    messages.success(request, 'Item added to cart successfully!')
                    return render(request, 'main.html', {'form': form, 'input_text': input_text, 'res': res})

    return render(request, 'main.html', {'form': form, 'input_text': input_text, 'res': res})

    #     # Modify the product_name and price based on your requirements
    #     product_name = (
    #         f"{input_text} - {selected_option}" if selected_option else "Default Product"
    #     )
    #     price = 10.00  # Modify this based on the actual price

    #     # Add the item to the cart
    #     if selected_option != "none":
    #         CartItem.objects.create(
    #             user=request.user, product_name=product_name, price=price
    #         )
    #     return render(request, "main.html", {"res": res})
    # return render(request, "main.html")
