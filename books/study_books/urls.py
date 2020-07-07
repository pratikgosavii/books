from django.contrib import admin
from django.urls import path, include
from . import views




urlpatterns=[

path('books_school', views.books_school_filter, name='books_school'),
path('books_college', views.books_college_filter, name='books_college'),
path('books_eng', views.books_eng_filter, name='books_eng'),
path('books_medical', views.books_medical_filter, name='books_medical'),

path('cart<book_id>', views.cart, name='cart'),

path('single-product<book_id>', views.single_product, name='single-product'),
]