from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContacForm

# Create your views here.
def contact(request):
    contact_form = ContacForm()

    if request.method == "POST":
        contact_form = ContacForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffetiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\n{}".format(name, email, content),
                "no-contestar@prueba.es",
                ["prueba@prueba.es"],
                reply_to=[email]
            )
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact') + "?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact') + "?fail")           

    return render(request, "contact/contact.html", {'form':contact_form})
