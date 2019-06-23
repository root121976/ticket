from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .forms import OrderForm
from .forms import TripInOrderForm

from .models import Book
from .models import Order
from .models import TripInOrder

from mysite.choices import *

# class Home(TemplateView):
#     count = User.objects.count()
#     template_name = 'home.html'
#     return render(request, 'home.html', {
#         'count': count
#     })

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

@login_required
def book_list(request):
    orders = Order.objects.all()
    return render(request, 'book_list.html', {
        'orders': orders
    })


def upload_book(request):

    if request.method == 'POST':

        form = OrderForm(request.POST, request.FILES,initial={'user': request.user})

        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = OrderForm(initial={'user': request.user})

    return render(request, 'upload_book.html', {
        'form': form
    })

def order_detailview(request,pk):
    order = Order.objects.get(pk=pk)

    if request.method == 'POST':

        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = OrderForm(instance=order)


    return render(request, 'order_detail.html', {
        'form': form
    })

def ticket_detailview(request,pk):
    ticket = TripInOrder.objects.get(pk=pk)

    if request.method == 'POST':

        form = TripInOrderForm(request.POST, request.FILES, instance=ticket)

        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = TripInOrderForm(instance=ticket)


    return render(request, 'ticket_detail.html', {
        'form': form
    })

def delete_book(request, pk):
    if request.method == 'POST':
        book = Order.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

def delete_trip(request, pk):
    if request.method == 'POST':
        book = TripInOrder.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

def create_trips(request, pk):

    order = Order.objects.get(pk=pk)

    if request.method == 'POST':

        form = TripInOrderForm(request.POST or None, initial={'order': order})

        if form.is_valid():
            form.save()

            return redirect('book_list')

    else:
        form = TripInOrderForm(request.POST, request.FILES, initial={'order': order})

    return render(request, 'create_trips.html', {
        'form': form
    })

class BookListView(ListView):
    model = Order
    template_name = 'class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'

def home(request):
    count = Order.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'
