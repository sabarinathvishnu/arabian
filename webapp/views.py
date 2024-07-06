from django.shortcuts import render,redirect
from arabapp.models import productdb,categorydb
from webapp.models import contactdb

# Create your views here.
def homepage(request):
    cat = categorydb.objects.all()
    return render(request,"home.html",{'category':cat})
def aboutpage(request):
    cat = categorydb.objects.all()
    return render(request,"about.html",{'category':cat})
def contactpage(request):
    cat = categorydb.objects.all()
    return render(request,"contact.html",{'category':cat})
def save_contact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        ph = request.POST.get('phone')
        obj = contactdb(name=na,email=em,subject=sub,message=msg,phone=ph)
        obj.save()
        return redirect(contactpage)





def ourproducts(request):
    pro = productdb.objects.all()
    cat = categorydb.objects.all()

    return render(request,"ourproducts.html",{'pro':pro,'cat':cat})
def filtered_products(request,cat_name):
    data = productdb.objects.filter(category=cat_name)
    return render(request,"products_filtered.html",{'data':data})
def singleproduct(request,proid):
    data = productdb.objects.get(id=proid)
    return render(request,"single_product.html",{'data':data})

