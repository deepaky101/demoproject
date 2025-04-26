from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def form_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = ProductForm()
        return render(request, 'form.html', {'form': form})