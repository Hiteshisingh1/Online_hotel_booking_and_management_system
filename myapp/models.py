from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ExtendedUser(models.Model):
    phone_number = models.CharField(max_length=15, default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=50, default=0)
    phone_number = models.CharField(max_length=15, default=0)
    email = models.EmailField(default=0)
    desc = models.CharField(max_length=1000, default=0)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=200, default="")
    location = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=50, default=0)
    hotel_image = models.ImageField(upload_to="images")
    distance = models.CharField(max_length=60, default="")
    info = models.CharField(max_length=2000, default="")
    img1 = models.ImageField(upload_to="images")
    img2 = models.ImageField(upload_to="images")
    img3 = models.ImageField(upload_to="images")
    img4 = models.ImageField(upload_to="images")

    def __str__(self):
        return self.hotel_name


class FinalBooking(models.Model):
    name = models.CharField(max_length=50, default="")
    user_name = models.CharField(max_length=50, default="")
    hotel_name = models.CharField(max_length=550, default="")
    amount = models.IntegerField(default=0)
    status = (
        ('Successful', 'Successful'),
        ('Failed', 'Failed'),
        ('Pending', 'Pending')
    )
    paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    address = models.CharField(max_length=1000, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    zip = models.IntegerField(default="")
    booking_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.name


class CorImg(models.Model):
    corimg1 = models.ImageField(upload_to="images")
    corimg2 = models.ImageField(upload_to="images")
    corimg3 = models.ImageField(upload_to="images")
