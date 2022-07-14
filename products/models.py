from django.db import models
from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'


    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        return self.name


    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
        null=True, blank=True)
    image = models.ImageField(max_length=1024, null=True, blank=True)


    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey('Product', related_name='reviews', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField('Reviews Section')
    author = models.ForeignKey(UserProfile, related_name='reviews', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.text


class Favourite(models.Model): 
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.product},favourite )'
