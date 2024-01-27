from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path("about/", views.about, name="about"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("contact/", views.contact, name="contact"),
    path("book/<int:id>/", views.book, name="book"),
    path("contact/", views.contact, name="contact"),
    path("otp/", views.otp, name="otp"),
    path("hotel/", views.hotel, name="hotel"),
    path("finalbook/", views.finalbook, name="finalbook"),
    path("hotel_desc/<int:id>/", views.hotel_desc, name="hotel_desc"),
    path("success/", views.success, name="success"),
    path("booking_info/", views.booking_info, name="booking_info"),
    path("delete/<int:id>", views.delete, name="delete"),

]
