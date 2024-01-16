from django.shortcuts import render
from .models import Contactus


# Create your views here.
def contact_us(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        subject = request.POST["subject"]

        contact = Contactus(name=name, phone=phone, email=email, subject=subject)
        contact.save()

    return render(request, "contact.html")
