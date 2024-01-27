# Generated by Django 3.1.4 on 2021-03-24 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=0, max_length=50)),
                ('phone_number', models.CharField(default=0, max_length=15)),
                ('email', models.EmailField(default=0, max_length=254)),
                ('desc', models.CharField(default=0, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CorImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corimg1', models.ImageField(upload_to='images')),
                ('corimg2', models.ImageField(upload_to='images')),
                ('corimg3', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='FinalBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('user_name', models.CharField(default='', max_length=50)),
                ('hotel_name', models.CharField(default='', max_length=550)),
                ('amount', models.IntegerField(default=0)),
                ('payment_status', models.CharField(choices=[('Successful', 'Successful'), ('Failed', 'Failed'), ('Pending', 'Pending')], default='', max_length=30)),
                ('phone_number', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=1000)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('zip', models.IntegerField(default='')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=200)),
                ('location', models.CharField(default='', max_length=50)),
                ('price', models.CharField(default=0, max_length=50)),
                ('hotel_image', models.ImageField(upload_to='images')),
                ('distance', models.CharField(default='', max_length=60)),
                ('info', models.CharField(default='', max_length=2000)),
                ('img1', models.ImageField(upload_to='images')),
                ('img2', models.ImageField(upload_to='images')),
                ('img3', models.ImageField(upload_to='images')),
                ('img4', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default=0, max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
