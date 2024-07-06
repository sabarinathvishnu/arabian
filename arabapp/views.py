from django.shortcuts import render,redirect
from arabapp.models import categorydb
from arabapp.models import productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def index_page(request):
    return render(request,"index.html")
def category_page(request):
    return render(request,"addcategory.html")
def save_categories(request):
    if request.method=="POST":
        cn = request.POST.get('cname')
        de = request.POST.get('description')
        img = request.FILES['image']
        obj=categorydb(categoryname=cn,descrption=de,product_image=img)
        obj.save()
        return redirect(category_page)
def display_product(request):
    data=categorydb.objects.all()
    return render(request,"displayproduct.html",{'data':data})
def edit_product(request,pid):
    data = categorydb.objects.get(id=pid)
    return render(request,"editproduct.html",{'data':data})
def update_product(request,pid):
    if request.method == "POST":
        cn = request.POST.get('cname')
        ds = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=pid).product_image
    categorydb.objects.filter(id=pid).update(categoryname=cn,descrption=ds,product_image=file)
    return redirect(display_product)
def delete_product(request,pid):
    data=categorydb.objects.filter(id=pid)
    data.delete()
    return redirect(display_product)
def product_page(request):
    cat = categorydb.objects.all()
    return render(request,"products.html",{'cat':cat})
def save_products(request):
    if request.method=="POST":
        cat = request.POST.get('category')
        pn = request.POST.get('pname')
        pr = request.POST.get('price')
        descr = request.POST.get('description')
        img = request.FILES['image']
        obj = productdb(category=cat, productname=pn, price=pr,description=descr,productimage=img)
        obj.save()
        return redirect(product_page)
def product_display(request):
    data2=productdb.objects.all()
    return render(request,"product_display2.html",{'data2':data2})
def product_edit(request,pid):
    data = productdb.objects.get(id=pid)
    cat = categorydb.objects.all()
    return render(request,"editproduct2.html",{'data':data,'cat':cat})
def contact_details(request):
    return render(request,"contactdata.html")
