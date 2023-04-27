from django.shortcuts import render,get_object_or_404,redirect
# from django.http import HttpResponse
from . models import Category,Product,Cart,relatedimage,contact
# Create your views here.
from .forms import signupform,signinform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import decimal
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    categories = Category.objects.filter(is_active=True, is_featured=True)[:5]
    products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request,'index.html',context)
   

def products(request):
    products = Product.objects.filter(is_active=True, is_featured=True)
    return render(request,"products.html",{'products':products})

def single(request):
    return render(request,"single-product.html")


# def contact(request):
#     return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def all_categories(request):
    categories=Category.objects.filter(is_active=True)
    return render(request,'category.html',{'categories':categories})

def category_products(request,slug):
    category=get_object_or_404(Category,slug=slug)
    products=Product.objects.filter(is_active=True,category=category)
    context={
        'category': category,
        'products':products
    }
    return render(request,'category_product.html',context)

def detail_page(request,slug):
    detail=get_object_or_404(Product,slug=slug)
    rimage=relatedimage.objects.filter(products=detail.id)
    context={
        'detail':detail,
        'rimage':rimage
    }
    return render(request,'detail_page.html',context)


@login_required
def cart(request):
    user=request.user
    cart_product=Cart.objects.filter(user=user)
    #display total on cart page
    amount=decimal.Decimal(0)
    shipamount=decimal.Decimal(10)
    cp=[p for p in Cart.objects.all() if p.user==user] #list comprehensive to calculate the total amount from the cart
    if cp:
        for x in cp:
            temp=(x.quantity*x.product.price)
            amount +=temp
    context={
        'cart_product':cart_product,
        'amount':amount,
        'shipamount':shipamount,
        'totalamount':amount+shipamount
    }
    return render(request,"cart.html",context)

def registration(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            # Saving with commit=False gets you a model object, then you can add your extra data and save it
            user.save()
            messages.info(request,'You can login')
        else:
            messages.info(request,'Please fill the form again')   
    else:
        form=signupform()
    context={
            'form':form
        } 
    return render(request,"form.html",context)

def login_page(request):
    if request.method=='POST':
        form=signinform(request.POST)
        username=form['username'].value()
        password=form['password'].value()
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid User")
    else:
        form=signinform()
    context={
        'form':form
    }
    return render(request,"signin.html",context)
@login_required
def logout_page(request):
    logout(request)
    return redirect('/')

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Product, id=product_id)

    # Check whether the Product is alread in Cart or Not
    item_already_in_cart = Cart.objects.filter(product=product_id, user=user)
    if item_already_in_cart:
        cp = get_object_or_404(Cart, product=product_id, user=user)
        cp.quantity += 1
        cp.save()
    else:
        Cart(user=user, product=product).save()

    return redirect('cart')
    
def pluscart(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        cp.quantity += 1
        cp.save()
    return redirect('cart')

def minuscart(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        if cp.quantity == 1:
            cp.delete()
        else:
            cp.quantity -= 1
            cp.save()
    return redirect('cart')

def remove(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        cp.delete()
    return redirect('cart')

def searchresult(request):
    q = request.GET.get('q','') 
    data = Product.objects.filter(title__icontains=q).order_by('-id') 
    return render(request,'searchpage.html',{'data':data})

@csrf_exempt
def contact_vie(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['comments']
        contact(Name=name,Email=email,Comments=phone).save()
        send_mail(subject='thankyou',message='thankyou for contacting us',from_email=settings.EMAIL_HOST_USER,recipient_list=[email,],fail_silently=False)
        messages.info(request,"Our Team will contact You Soon.")
    return render(request,'contact.html')


