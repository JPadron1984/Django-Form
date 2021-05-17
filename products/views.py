from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .forms import ProductForm,RawProductForm
# Create your views here.


def home_view(request):

    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)
            my_form = RawProductForm()

    queryset = Product.objects.all()

    context = {
        'form': my_form,
        'object_list': queryset
    }
    return render(request, "home.html", context)


def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)
            my_form = RawProductForm()


    context = {
        "form": my_form
    }
    return render(request, "home.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context ={
        "object_list":queryset
    }
    return render(request, "home.html",context)

