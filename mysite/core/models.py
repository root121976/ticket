from django.db import models
from django.contrib.auth.models import User
from mysite.choices import *

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

class BookRazdel(models.Model):
    book = models.ForeignKey(Book, blank=True, null=True, default=None,on_delete=models.CASCADE)
    razdel = models.CharField(max_length=64, blank=False, null=True, default=None)


    def __str__(self):
        return self.razdel



class Customer(models.Model):
    #user = models.ForeignKey(User, blank=True, null=True, default=None,on_delete=models.CASCADE)

    customer_lastname = models.CharField(max_length=64, blank=False, null=True, default=None)
    customer_firstname = models.CharField(max_length=64, blank=False, null=True, default=None)
    customer_patronymic = models.CharField(max_length=64, blank=False, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=10, blank=False, null=True, default=None)
    #паспорт
    customer_id_number = models.DecimalField(max_digits=10,decimal_places=0,blank=False,null=True, default=None)
    #дата рождения
    customer_bday = models.DateField(blank=False, null=True, default=None)
    #должность
    customer_position = models.CharField(max_length=64, blank=False, null=True, default=None)
    #подразделение
    customer_division = models.CharField(max_length=64, blank=False, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s %s" % (self.customer_lastname, self.customer_firstname, self.customer_patronymic)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

# class Status(models.Model):
#     name = models.IntegerField(choices=STATUS_CHOICES, default=1)
#
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     def __str__(self):
#         return  self.name
#
#     class Meta:
#         verbose_name = 'Статус заказа'
#         verbose_name_plural = 'Статусы заказа'

class Order(models.Model):

    user = models.ForeignKey(User, blank=True, null=True, default=None,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,blank=False, null=True, on_delete=models.CASCADE,default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    # status = models.ForeignKey(Status,on_delete=models.CASCADE)
    status =  models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)


class TripInOrder(models.Model):

    order = models.ForeignKey(Order, blank=True, null=False, default=None,on_delete=models.CASCADE)
    date_of_trip = models.DateField(blank=False,null=True, default=None)
    time_of_trip = models.IntegerField(choices=TIME_CHOICES, default=0)
    departure = models.CharField(max_length=50, blank=True, null=True, default=None)
    arrival = models.CharField(max_length=50, blank=True, null=True, default=None)
    ticket_number = models.CharField(max_length=24, blank=True, null=True, default=None)
    flight_number = models.CharField(max_length=24, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    # status = models.ForeignKey(Status, on_delete=models.CASCADE,default=None,null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    pdf = models.FileField(upload_to='books/pdfs/',blank=True, null=True, default=None)

    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s %s" % (self.date_of_trip.strftime('%Y-%m-%d'), self.departure, self.arrival)

    class Meta:
        verbose_name = 'Поездка'
        verbose_name_plural = 'Поездки'

