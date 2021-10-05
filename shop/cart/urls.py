from django.urls import path
from .import views

app_name = 'cart'

urlpatterns = [

    path('', views.cartView, name='cart'),
    path('add/', views.addToCart , name='add'),
    path('delete/<int:product_id>/<int:qty>', views.deleteCartItem , name='delete'),
    path('remove/', views.removeCart, name='remove'),
    path('order/add/<int:cart_id>', views.addOrder, name='add_order')

]