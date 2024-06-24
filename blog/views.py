from django.shortcuts import render,get_object_or_404
from .form import EmailForm
from blog.models import Client,Email


def index(request):
    form = EmailForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    ol = Client.objects.all()
    email = Email.objects.all()
    context = {
         "ol": ol,
         "email": email
    }
    return render(request, "index.html", context=context)



def index_detel(request,id):
    client = get_object_or_404(Client,id=id)
    context={
        "detel":client
    }
    return render(request,"detel.html",context=context)