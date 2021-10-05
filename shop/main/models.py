from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField('Nomi',max_length=100,)
	slug = models.SlugField('*',max_length=100, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Kategoriya'
		verbose_name_plural = 'Kategoriyalar'
		ordering = ['name']

class Colors(models.Model):
	COLORS = (
	('white','WHITE'),
	('black','BLACK'),
	('blue','BLUE'),
	('green','GREEN'),
	('yellow','YELLOW'),
	('red','RED'),
	('tomato','TOMATO'),
	('pink','PINK'),
	('teal','TEAL'),
	('brown','BROWN'),
	)
	color = models.CharField('Rang nommi', max_length=50, choices=COLORS)
	def __str__(self):
		return self.color

class Product(models.Model):
	COLORS = (
	('white','WHITE'),
	('black','BLACK'),
	('blue','BLUE'),
	('green','GREEN'),
	('yellow','YELLOW'),
	('red','RED'),
	('tomato','TOMATO'),
	('pink','PINK'),
	('teal','TEAL'),
	('brown','BROWN'),
	)
	name = models.CharField('Nomi',max_length=100,)
	slug = models.SlugField('*',max_length=100, unique=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
	image = models.ImageField('Rasmi',upload_to="product_images/")
	description = models.TextField('Tovar haqida', blank=True)
	price = models.PositiveIntegerField('Narxi', default=0, null=True)
	old_price = models.PositiveIntegerField('Avvalgi Narxi', default=0, blank=True)
	colors = models.CharField('Ranglari', max_length=50, choices=COLORS )
	other_colors = models.ManyToManyField(Colors,related_name='other_colors')
	instock = models.BooleanField("Omborda bor yoki yo'q", default=True)
	count = models.PositiveIntegerField('Soni', default=1)
	views = models.PositiveIntegerField('Soni', default=100)

	class Meta:
		verbose_name = 'Tovar'
		verbose_name_plural = 'Tovarlar'
		ordering = ['-id']

	def __str__(self):
		return f"Tovar - {self.name}"



# Product Images model
class ProductImages(models.Model):
	product = models.ForeignKey(Product,
		default=None,
		null=True,
		blank=True,
		on_delete=models.CASCADE,
		related_name='product_images')
	image = models.ImageField('Tovar alohida rasmlari',
		upload_to='product_images/',
		blank=True, null=True,)

	def __str__(self):
		return self.product.name

	class Meta:
		verbose_name = 'Tovar rasmlari'
		verbose_name_plural = 'Tovar rasmlari'