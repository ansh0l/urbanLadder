from django.db import models
from product.models import Product
from customer.models import Customer

class Order(models.Model):
    customer = models.ForeignKey(Customer)
    date = models.DateTimeField(auto_now=True, null = True)
    amount = models.FloatField(blank = True)
    payment_method = models.CharField(max_length = 20, default = 'cc', choices=(
        ('cod','cash on delivery'),
        ('cc','credit card'),
        ('nb','net banking')))
    payment_realised = models.BooleanField(default = False)

    def calculate_amount(self):
        oi_list = OrderItem.objects.filter(order = self.pk)
        amt = float(0) 
        for oi in oi_list:
            amt += oi.product.price * oi.quantity
        return amt

    def get_order_items(self):
        return OrderItem.objects.filter(order = self.pk)


    def save(self, *args, **kwargs):
        if self.payment_method in ['cc', 'nb']:
            self.payment_realised = True
        self.amount = self.calculate_amount()
        super(Order, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.customer) + " bought worth " + str(self.amount) + " on " + str(self.date)

class OrderItem(models.Model):
    quantity = models.IntegerField(default = 1)
    product = models.ForeignKey(Product) 
    order = models.ForeignKey(Order)
    
    def save(self, *args, **kwargs):
        super(OrderItem, self).save(*args, **kwargs)
        self.order.save()
    
    def __unicode__(self):
        return str(self.quantity) + " of " + str(self.product) + " for order " + str(self.order.pk)
