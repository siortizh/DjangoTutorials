from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import render, redirect




# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'



class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Sara Isabel Ortiz",
        })

        return context


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact - Online Store",
            "subtitle": "contact us",
            "contact_info": {
                'email': 'contacto@ejemplo.com',
                'address': 'Calle Falsa 123, Ciudad Ficticia',
                'phone number': '+123 456 7890',
            },
        })
        return context


class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV"},
        {"id":"2", "name":"iPhone", "description":"Best iPhone"},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast"},
        {"id":"4", "name":"Glasses", "description":"Best Glasses"}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] =  "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            product = Product.products[int(id) - 1]
        except IndexError:
            # Si el número de producto no es válido, redirige al usuario a la página de inicio
            return HttpResponseRedirect(reverse('home'))

        viewData = {
            "title": product["name"] + " - Online Store",
            "subtitle": product["name"] + " - Product information",
            "product": product,
        }

        return render(request, self.template_name, viewData)

class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 499.99},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 899.99},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 39.99},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 19.99}
    ]


class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)


class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            
            return redirect(form) 
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
