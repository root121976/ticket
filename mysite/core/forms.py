from django import forms
from mysite.choices import *

import datetime

from .models import Book, Order, TripInOrder

class OrderForm(forms.ModelForm):

    status = forms.ChoiceField(choices=STATUS_CHOICES, label="", initial='', widget=forms.Select(), required=True)
    class Meta:
        model = Order
        exclude = ('updated','comments')
        widgets = {'user': forms.HiddenInput()}



class DateInput(forms.DateInput):
    input_type = 'date'

class TripInOrderForm(forms.ModelForm):

    status = forms.ChoiceField(choices=STATUS_CHOICES, label="", initial='', widget=forms.Select(), required=True)

    class Meta:
        model = TripInOrder
        exclude = ('updated',)
        widgets = {
            'date_of_trip': DateInput(),
        }

    date_of_trip = forms.DateField(widget=DateInput, initial=datetime.date.today)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf', 'cover')