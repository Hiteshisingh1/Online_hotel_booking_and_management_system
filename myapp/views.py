from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.template import context

from .models import ExtendedUser, Contact, Hotel, FinalBooking, CorImg
from django.shortcuts import render
import razorpay
from datetime import datetime
import random
from twilio.rest import Client


def index(request):
    img = CorImg.objects.all()
    return render(request, "home.html", {'img': img})


def about(request):
    return render(request, "about.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('/home/register/')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'this email is already registered to other account')
                return redirect('/home/register/')
            else:

                phone_number = request.POST.get('phone_number', '')
                request.session['phone_number'] = phone_number
                if ExtendedUser.objects.filter(phone_number=phone_number).exists():
                    messages.error(request, 'This phone number is linked with other account!')
                    return redirect('/home/register/')
                else:

                    # importing twilio

                    # Your Account Sid and Auth Token from twilio.com / console
                    account_sid = 'AC31381dac1791b7c4ad8c6863c15ddc87'
                    auth_token = 'd382f86795f5640d230cce94191ba815'

                    client = Client(account_sid, auth_token)

                    def random_with_N_digits(n):
                        range_start = 10 ** (n - 1)
                        range_end = (10 ** n) - 1
                        return random.randint(range_start, range_end)

                    otp = str(random_with_N_digits(6))
                    request.session['otp'] = otp

                    ''' Change the value of 'from' with the number
                    received from Twilio and the value of 'to'
                    with the number in which you want to send message.'''
                    message = client.messages.create(
                        from_='+18564062788',
                        body="Your OTP is : " + otp,
                        to='+91' + phone_number
                    )
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                    email=email, password=password1)
                    user.save()
                    newExtendedUser = ExtendedUser(phone_number=phone_number, user=user)
                    newExtendedUser.save()
                    return redirect('/home/otp/')

        else:
            messages.error(request, 'password does not match')
            return redirect('/home/register/')
    return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        global user1

        def user1():
            return username

        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful')
            return redirect('/home/')
        else:
            messages.error(request, 'invalid information')
            return redirect('/home/login/')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/home/')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        phone_number = request.POST.get('phone_number', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')

        contact_us = Contact(name=name, phone_number=phone_number, email=email, desc=desc)
        contact_us.save()
    return render(request, "contact.html")


def otp(request):
    if request.method == "POST":
        otp = request.POST.get('otp', '')
        otp2 = request.session['otp']
        if otp is not None:
            if otp == otp2:
                messages.success(request, "OTP confirmed")
                return redirect("/home/login/")
            else:
                messages.error(request, "Entered Wrong OTP")
                return redirect("/home/otp/")
    return render(request, "otp.html")


def hotel(request):
    if request.method == "POST":
        loc = request.POST.get('location', '')
        hotel = Hotel.objects.filter(location=loc)
        return render(request, "hotel.html", {'hotel': hotel})


def book(request, id):
    hotel = Hotel.objects.filter(id=id)
    return render(request, "book.html", {'hotel': hotel})


def finalbook(request):
    name = request.POST.get('name', '')
    username = user1()
    amount = int(request.POST.get('amount', ''))
    id = request.POST.get('id', '')
    hotel_name = request.POST.get('hotel_name', '')
    phone_number = request.POST.get('phone_number', '')
    email = request.POST.get('email', '')
    address = request.POST.get('address', '')
    city = request.POST.get('city', '')
    zip = request.POST.get('zip', '')
    state = request.POST.get('state', '')
    booking_date = datetime.now()

    client = razorpay.Client(auth=('rzp_test_zfSTgE8lnvhooF', 'qOdiPcMr5aJ4L6IoP0YrX2Q8'))
    payment = client.order.create({'amount': amount * 100, 'currency': 'INR',
                                   'payment_capture': '1'})
    order_id = payment['id']
    order_status = payment['status']

    if order_status == 'created':
        finalbook = FinalBooking(name=name, phone_number=phone_number, email=email, address=address, city=city, zip=zip,
                                 state=state, amount=amount, id=id, hotel_name=hotel_name, user_name=username,
                                 booking_date=booking_date, order_id=order_id)
        finalbook.save()
        payment['username'] = username

    print(order_id)
    return render(request, "payment.html", {'payment': payment})


def hotel_desc(request, id):
    hotel = Hotel.objects.filter(id=id)
    return render(request, "hotel_desc.html", {'hotel': hotel})


def success(request):
    response = request.POST
    param_dict = {
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    client = razorpay.Client(auth=('rzp_test_zfSTgE8lnvhooF', 'qOdiPcMr5aJ4L6IoP0YrX2Q8'))
    try:
        status = client.utility.verify_payment_signature(param_dict)
        finalbook = FinalBooking.objects.get(order_id=response['razorpay_order_id'])
        finalbook.razorpay_payment_id = response['razorpay_payment_id']
        finalbook.paid = True
        finalbook.save()
        account_sid = 'AC31381dac1791b7c4ad8c6863c15ddc87'
        auth_token = 'd382f86795f5640d230cce94191ba815'

        client = Client(account_sid, auth_token)
        ''' Change the value of 'from' with the number
            received from Twilio and the value of 'to'
            with the number in which you want to send message.'''
        message = client.messages.create(
            from_='+18564062788',
            body="Congratulations your booking has been confirmed and your order id = " + response['razorpay_order_id'],
            to='+918291636142'
        )
        return render(request, "success.html", {'status': True})
    except:
        return render(request, "success.html", {'status': False})


def booking_info(request):
    user = user1()
    hotel = FinalBooking.objects.filter(user_name=user)
    return render(request, "booking_info.html", {'hotel': hotel})


def delete(request, id):
    booking = FinalBooking.objects.filter(id=id)
    booking.delete()
    account_sid = 'AC31381dac1791b7c4ad8c6863c15ddc87'
    auth_token = 'd382f86795f5640d230cce94191ba815'

    client = Client(account_sid, auth_token)
    ''' Change the value of 'from' with the number
        received from Twilio and the value of 'to'
        with the number in which you want to send message.'''
    message = client.messages.create(
        from_='+18564062788',
        body="your request for cancellation the booking has been confirmed ",
        to='+918291636142'
    )
    return redirect("/home/booking_info/")
