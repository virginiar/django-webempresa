from django.shortcuts import render
from .forms import ContacForm

# Create your views here.
def contact(request):
    contact_form = ContacForm()
    return render(request, "contact/contact.html", {'form':contact_form})
