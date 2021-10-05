from django.urls import path
from .import views


app_name = 'main'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('detail/<slug>',views.ProductDetailView.as_view(),name='detail'),
    path('category/detail/<slug>',views.CategoryDetailView.as_view(),name='category_detail'),
    path('accounts/profile/', views.profile, name='profile'),
    path('searchs/',views.searchResults, name='searchs'),

]