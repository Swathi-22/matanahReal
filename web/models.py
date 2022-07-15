
from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from tinymce.models import HTMLField



class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=150)
    message=models.TextField()

    def __str__(self):
        return self.name    


class Gallery(models.Model):
    image = VersatileImageField('Image',upload_to='gallery/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("Gallery")

    def __str__(self):
        return str(self.image)


class Category(models.Model):
    title=models.CharField(max_length=50)
    # is_active=models.BooleanField(default=True)
    slug=models.SlugField(unique=True)
    

    def __str__(self):
        return self.title


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=225)
    image = VersatileImageField('Image',upload_to='product/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')
    is_popular=models.BooleanField(default=False)
    is_featured=models.BooleanField(default=False)
    

    def __str__(self):
        return self.title




class Ad1(models.Model):
    image = VersatileImageField('Image',upload_to='Ad/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')


    class Meta:
        verbose_name_plural = ("Advertisement 1")

    def __str__(self):
        return str(self.image)



class Ad2(models.Model):
    image = VersatileImageField('Image',upload_to='Ad/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')


    class Meta:
        verbose_name_plural = ("Advertisement 2")

    def __str__(self):
        return str(self.image)