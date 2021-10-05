from .models import Category,Product
from cart.models import Cart

def view_all(request):
	try:
		cart = Cart.objects.get(id=request.session.get('user_cart_id'))
	except:
		cart = {'status':'Savatcha topilmadi!'}
	print(cart)
	
	category = Category.objects.all()
	post = Product.objects.all().order_by('?')[:6]


	context = {
		'categories':category,
		'posts':post,
		'cart':cart,
	}

	return context