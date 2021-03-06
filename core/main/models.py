from django.db import models

class Category(models.Model):
    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catbrand')
    name = models.CharField('Brand name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='carbrend', null=True)
    name = models.CharField('Car name', max_length=30)
    year = models.IntegerField('Car year')
    about = models.TextField('Car about', null=True)
    price = models.IntegerField('Car price')
    img = models.ImageField('Car image', upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
