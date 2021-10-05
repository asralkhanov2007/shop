from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.views.generic import (
	TemplateView,
	ListView,
	DetailView
	)
from .models import *
# Create your views here.

class CategoryDetailView(DetailView):
	model = Category
	template_name = 'category.html'
	
	
class HomePageView(ListView):
	model = Product
	paginate_by = 12
	template_name = 'index.html'


class ProductDetailView(DetailView):
	model = Product
	template_name = 'single-product.html'
	def get_object(self):
	    obj = super().get_object()
	    obj.views += 1
	    obj.save()
	    return obj

def profile(request):
	return render(request, 'account/profile.html')


def searchResults(request):
    q = request.GET.get('query', None)
    posts = Product.objects.filter(name__icontains=q)


    return render(request,'results.html',{'posts':posts})


