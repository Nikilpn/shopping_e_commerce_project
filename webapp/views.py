from django.shortcuts import render,redirect
from Backend.models import productdb
from Backend.models import categorydb
from webapp.models import contactdb
from webapp.models import Registerdb
from django.contrib import messages
from webapp.models import cartdb,Orderdb
import razorpay


# Create your views here.
def home_page(request):
    cat=categorydb.objects.all()
    return render(request,"home.html",{'cat':cat})


def blog_page(request):
    cat = categorydb.objects.all()
    return render(request,"blog.html",{'cat':cat})
def contact_page(request):
    cat = categorydb.objects.all()
    return render(request,"contact.html",{'cat':cat})



def our_products(request):
    cat = categorydb.objects.all()
    pro=productdb.objects.all()
    return render(request,"our_products.html",{'products':pro,'cat':cat})





#saving in to database

def save_contact(request):
    if request.method=="POST":
        cn=request.POST.get('cname')
        ce = request.POST.get('cemail')
        cmo = request.POST.get('cmobile')
        cme = request.POST.get('cmessage')

        obj = contactdb(CONTACTNAME=cn,CONTACTEMAIL=ce,CONTACTMOBILE=cmo ,CONTACTMESSAGE=cme)
        obj.save()
        return redirect(contact_page)



#for getting category of similar products

def product_filtered(request,cat_name):
    cat = categorydb.objects.all()
    data=productdb.objects.filter(CATEGORY=cat_name)
    return render(request,"products_filtered.html",{'data':data,'cat':cat})

def single_products(request,pro_id):
    cat = categorydb.objects.all()
    data=productdb.objects.get(id=pro_id)
    return render(request,"single_product.html",{'data':data,'cat':cat})
def registration_page(request):
    return render(request, "Register.html")


def save_registration_page(request):
    if request.method == "POST":
        na = request.POST.get('rname')
        em = request.POST.get('remail')
        pa = request.POST.get('rpassword')
        cpa = request.POST.get('rconfirmpassword')
        obj = Registerdb(REGISTERNAME=na, REGISTEREMAIL=em, REGISTERPASSWORD=pa, REGISTERCONFIRMPASSWORD=cpa)
        if Registerdb.objects.filter(REGISTERNAME=na).exists():
            messages.warning(request,"Username already exists")
            return redirect(registration_page)


        elif Registerdb.objects.filter(REGISTEREMAIL=em).exists():
            messages.warning(request, "Email already exists")
            return redirect(registration_page)
        else:
            obj.save()
            messages.success(request,"Registerd successfully")
        return redirect(registration_page)

def User_login(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pswd = request.POST.get('upassword')
        if Registerdb.objects.filter(REGISTERNAME=un,REGISTERPASSWORD=pswd).exists():
            request.session['REGISTERNAME'] = un
            request.session['REGISTERPASSWORD'] = pswd
            messages.success(request,"login successfully")
            return redirect(home_page)
        else:
            messages.error(request, "login failed")
            return redirect(registration_page)
    else:
        messages.warning(request, "login failed")
        return redirect(registration_page)
def user_logout(request):
    del request.session['REGISTERNAME']
    del request.session['REGISTERPASSWORD']
    messages.success(request, "logot successfully")
    return redirect(home_page)


def save_cart(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pn=request.POST.get('productname')
        qn=request.POST.get('quantity')
        tr=request.POST.get('totalprice')
        obj=cartdb(USERNAME=un,PRODUCTNAME=pn,QUANTITY=qn,TOTALPRICE=tr)
        obj.save()
        messages.success(request, "saved to cart ")
        return redirect(home_page)
def cart_page(request):
    cat = categorydb.objects.all()
    data=cartdb.objects.filter(USERNAME=request.session['REGISTERNAME'])
    subtotal=0
    shipping_charge=0
    total=0
    for d in data:
        subtotal=subtotal+d.TOTALPRICE
        if subtotal<=1500:
            shipping_charge=150
        else:
            shipping_charge=50
        total=subtotal+shipping_charge
    return render(request,"cart.html",{'data':data,'cat':cat,'subtotal':subtotal,'shipping_charge':shipping_charge,'total':total})

def delete_item(request,p_id):
    x=cartdb.objects.filter(id=p_id)
    x.delete()
    messages.success(request, "item deleted")
    return redirect(cart_page)

#user login page
def user_login_page(request):
    return render(request,"user_login.html")
def checkout_page(request):
    cat = categorydb.objects.all()
    products = cartdb.objects.filter(USERNAME=request.session['REGISTERNAME'])
    subtotal = 0
    shipping_charge = 0
    total_amount = 0
    for i in products:
        subtotal = subtotal + i.TOTALPRICE
        if subtotal >= 500:
            shipping_charge = 50
        else:
            shipping_charge = 100
        total_amount = subtotal + shipping_charge


    return render(request,"checkout.html",{'products':products,'shipping_charge':shipping_charge,'subtotal':subtotal,'total_amount':total_amount,'category':cat})
def save_billingaddress(request):
    if request.method=="POST":
        na=request.POST.get('bname')
        em = request.POST.get('bemail')
        ad = request.POST.get('baddress')
        ph = request.POST.get('bphone')
        pr = request.POST.get('bprice')
        me = request.POST.get('bill')
        obj=Orderdb(BILLINGNAME=na,BILLINGEMAIL=em,BILLINGADDRESS=ad,BILLINGPHONE=ph,BILLINGPRICE=pr,BILLINGMESSAGE=me)
        obj.save()
        return redirect(paymentpage)

def paymentpage(request):
    #retrieve the orderdb object with the specified id
    customer=Orderdb.objects.order_by('-id').first()

    #get the payment amount of the specified customer
    payy=customer.BILLINGPRICE

    #convert the amount to paisa(smallest currency unit)
    amount=int(payy*100)

    #convert amount to string for printing
    payy_str=str(amount)

    #printingeach character of the payment amount
    for i in payy_str:
        print(i)
    if request.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_klfWwvjaFXjXmC','s9P7dwOwYckK352FfRJOXIRV'))
        payment=client.order.create({'amount':amount,'currency':order_currency,'payment_capture':'1'})
    return render(request,"payment.html",{'customer':customer,'payy_str':payy_str})