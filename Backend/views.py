from django.shortcuts import render,redirect
from Backend.models import categorydb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate,login
from webapp.models import contactdb
from django.contrib import messages


# Create your views here.
def index_page(request):
    return render(request,"index.html")

def add_category(request):
    return render(request,"add_category.html")

def save_category(request):
    if request.method=="POST":
        cn=request.POST.get('cname')
        cd = request.POST.get('cdescription')
        img = request.FILES['cimage']
        obj=categorydb(CATEGORYNAME=cn,CATEGORYDESCRIPTION=cd,CATEGORYIMAGE=img)
        obj.save()
        messages.success(request,"category saved successfully")
        return redirect(add_category)

def display_category(request):
    data=categorydb.objects.all()
    return render(request,"display_category.html",{'data':data})

def edit_category(request,edit_id):
    data=categorydb.objects.get(id=edit_id)
    return render(request,"edit_category.html",{'data':data})


def update_category(request,up_id):
    if request.method==("POST"):
        cn=request.POST.get('cname')
        cd=request.POST.get('cdescription')

        try:
            img=request.FILES['cimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=up_id).CATEGORYIMAGE
        categorydb.objects.filter(id=up_id).update(CATEGORYNAME=cn,CATEGORYDESCRIPTION=cd,CATEGORYIMAGE=file)
        messages.success(request, "category updated successfully")
        return redirect(display_category)
def delete_category(request,del_id):
    x=categorydb.objects.filter(id=del_id)
    x.delete()
    messages.error(request, "deleted..")
    return redirect(display_category)
def login_page(request):
    return render(request,"admin_login.html")

def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request, "welcome..")
                return redirect(index_page)
            else:
                messages.error(request, "invalid password.")
                return redirect(login_page)
        else:
            messages.warning(request, "user not found.")
            return redirect(login_page)



def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.warning(request, "logout successfully")
    return redirect(login_page)

# ********************************

def products_page(request):
    cat=categorydb.objects.all()
    return render(request,"products.html",{'cat':cat})

#******** function for saving in to productdb
def save_product(request):
    if request.method=="POST":
        cn=request.POST.get('cname')
        pn = request.POST.get('pname')
        pr = request.POST.get('pprice')
        pd = request.POST.get('pdescription')
        img = request.FILES['pimage']
        obj = productdb(CATEGORY=cn,PRODUCTNAME=pn,PRODUCTPRICE=pr ,PRODUCTDESCRIPTION=pd, PRODUCTIMAGE=img)
        obj.save()
        messages.success(request, "product saved successfully")
        return redirect(products_page)

def display_product(request):
    data=productdb.objects.all()
    return render(request,"display_product.html",{'display':data})

#************* edit product page

def edit_product(request,edit_id):
    edit=productdb.objects.get(id=edit_id)
    cat=categorydb.objects.all()
    return render(request,"edit_product.html",{'edit':edit,'cat':cat})

def update_product(request,up_id):
    if request.method==("POST"):
        cn = request.POST.get('cname')
        pn=request.POST.get('pname')
        pr = request.POST.get('pprice')
        pd=request.POST.get('pdescription')

        try:
            img=request.FILES['pimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=up_id).PRODUCTIMAGE
        productdb.objects.filter(id=up_id).update(CATEGORY=cn,PRODUCTNAME=pn,PRODUCTPRICE=pr,PRODUCTDESCRIPTION=pd,PRODUCTIMAGE=file)
        messages.success(request, "product updated successfully")
        return redirect(display_product)



def delete_product(request,del_id):
    x=productdb.objects.filter(id=del_id)
    x.delete()
    messages.error(request,"deleted..")
    return redirect(display_product)

def contact_details(request):
    data=contactdb.objects.all()
    return render(request,"contact_data.html",{'data':data})

def delete_contact(request,del_id):
    x=contactdb.objects.filter(id=del_id)
    x.delete()
    return redirect(contact_details)



