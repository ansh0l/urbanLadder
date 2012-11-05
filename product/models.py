from django.db import models
from django.template.defaultfilters import slugify

#class Feature(models.Model):
#    name = models.CharField(max_length=100)
#    description = models.TextField() 
#    
#    def __unicode__(self):
#        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    price = models.FloatField()
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

#class ProductFeatureMap(models.Model):
#    feature = models.ForeignKey(Feature)    
#    product = models.ForeignKey(ProductInfo)    
#    
#    def __unicode__(self):
#        return self.feature + self.product
