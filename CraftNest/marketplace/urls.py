from django.urls import path
from marketplace import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('product/',views.product_list,name='product_list'),
    path('contact/',views.contact,name='contact'),
]