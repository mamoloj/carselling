
from django.shortcuts import render , redirect
from django.contrib.auth.models import User  
from .forms import CarForm , BuyCarForm , LoginForm
from django.core.paginator import Paginator 
from .models import Car , BuyCar
from .filters import CarFilter
from django.contrib.auth import  login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
def cars_list(request):
    page_name = "List a Car"
    form = CarForm()

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('thank_you',data.id)


    
    context = {
    'form' : form,
    'page_name' : page_name
    } 
    return render(request, 'car_list.html',context)  


def thank_you(request,id):
    page_name = "Car is now Listed!"

    context = {
    'id' : id,
    'page_name' : page_name
    } 
    return render(request, 'thank_you.html',context)  



def find_cars(request):
    page_name = "Listed Cars"

    filtered_cars = CarFilter(request.GET,queryset=Car.objects.all().order_by('-created_on'))
    
    paginated_filtered_cars =  Paginator(filtered_cars.qs,10)
    page_num = request.GET.get('page',1)
    try:
        page = paginated_filtered_cars.page(page_num)
    except :
        page = paginated_filtered_cars.page(1)
    context = {
    'items' : page,
    'page_name' : page_name,
    'filtered_cars' :filtered_cars,
    } 
    return render(request, 'listed_cars.html',context)  


def buy_car(request,id):
    car_obj = Car.objects.filter(id=id)
    if not car_obj :
        return redirect('find_cars')
    page_name = "Buy a Car"
    form = BuyCarForm()
    if request.method == 'POST':
        form = BuyCarForm(request.POST)
        

        if form.is_valid():
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            car_obj[0].sold = True
            car_obj[0].save()
            buyer_car = BuyCar.objects.create(name=name,mobile=mobile,car=car_obj[0])
            send_email(buyer_car.id)
            return redirect('buy_success')
            
    
    context = {
    'page_name' : page_name,
    'form' : form,
    'id' : id
    } 
    return render(request, 'buy_car.html',context)  


def buy_success(request):
    page_name = "Thank you for buying!"

    context = {
    'page_name' : page_name
    } 
    return render(request, 'buy_success.html',context)  

def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user

    return None
def login_user(request):
    logout(request)
    page_name = "User login"
    form = LoginForm()
    if request.method == 'POST' :
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate_user(email, password)  

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('find_cars')
            else:
                messages.error(request,'Invalid Credentials')

    context = {
    'page_name' : page_name,
    'form' : form
    } 
    return render(request, 'login.html',context)  


def logout_user(request):
	logout(request)
	return redirect('find_cars')

@login_required()
def make_available(request,id):
    car_obj = Car.objects.filter(id=id)
    if car_obj :
        car_obj[0].sold = False
        car_obj[0].save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def send_email(id):
    subject = "Someone wants to buy a car"
    buyer = BuyCar.objects.filter(id=id)
    if buyer :
        buyer = buyer.first()
        commision = buyer.car.price * 0.05
        net_amount = buyer.car.price - commision
        message = """
        SELLER NAME : {0}
        SELLER MOBILE : {1}
        CAR MAKE : {2}
        CAR MODEL : {3}
        CAR YEAR : {4}
        CAR CONDITION : {5}
        CAR PRICE : ${6}
        BUYER NAME : {7}
        BUY MOBILE : {8}
        COMMISION : ${9}
        NET AMOUNT TO SELLER : ${10}
        """.format(buyer.car.name,
                    buyer.car.mobile,
                    buyer.car.make,
                    buyer.car.model,
                    buyer.car.year,
                    buyer.car.condition,
                    buyer.car.price,
                    buyer.name,
                    buyer.mobile,
                    round(commision,2),
                    round(net_amount,2)
                )
        send_mail(subject, message,settings.DEFAULT_FROM_EMAIL, ['mamoloj@gmail.com'])