from django.shortcuts import render
from .models import Product, Contact
from math import ceil


# For Product objects to show use the following code
# ctrl+shift+p > Preferences: Configure Language Specific Settings > Python
# "python.linting.pylintArgs": [
#         "--load-plugins=pylint_django",
#     ]


# Create your views here.
from django.http import HttpResponse

def index(request):
    #products = Product.objects.all()
    #print(products)
    #n = len(products)
    
    # params = {'no_of_slides': nslides, 'range': range(nslides), 'product': products}
    #allprods = [[products, range(1,nslides), nslides],
    #            [products, range(1,nslides), nslides]]
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1, nslides), nslides])

    params = {'allprods' : allprods}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')
    
def contact(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return HttpResponse("we are tracker")

def search(request):
    return HttpResponse("we are search")

def productView(request, myid):
    # Fetch the product using id 
    product = Product.objects.filter(id = myid)
    print(product)
    return render(request, 'shop/prodview.html', {'product':product[0]})

def checkout(request):
    return HttpResponse("we are checkout")