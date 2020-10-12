from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Image(models.Model):
    name= models.CharField(max_length=50)
    description = HTMLField()
    gallery_image = models.ImageField(upload_to='pics/', blank=True)
    categories = models.ManyToManyField(Categories)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name
        
    @classmethod
    def all_images(cls, self):

        return Image.objects.all()

    @classmethod
    def search_by_category(cls,search_images):
        images = Image.objects.filter(categories__name__icontains=search_images)
        return images

    @classmethod
    def view_location(cls,name):
        location = cls.objects.filter(location=name)
        return location

    @classmethod
    def view_category(cls,cat):
        categories = cls.objects.filter(categories=cat)
        return categories

    class Meta:
        ordering = ['name']
