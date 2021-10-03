from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
    products=Products.objects.all()
    data={'products':products}
    return render(request, 'index.html',data)

def contact(request):
    return render(request, 'contact.html')