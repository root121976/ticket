from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/viewdetail', views.order_detailview, name='order_detailview'),
    path('books/<int:pk>/ticket_viewdetail', views.ticket_detailview, name='ticket_detailview'),
    path('books/<int:pk>/deletebook', views.delete_book, name='delete_book'),
    path('books/create/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/addtrip/', views.create_trips, name='create_trips'),
    path('books/<int:pk>/delete/', views.delete_trip, name='delete_trip'),



    path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),



    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)