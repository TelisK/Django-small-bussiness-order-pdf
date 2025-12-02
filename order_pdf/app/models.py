from django.db import models

# Create your models here.
class Content(models.Model):
    ORDER_TYPES = [
    ('Order', 'Order'),
    ('Return', 'Return'),
    ]
    order_type = models.CharField(max_length=20, choices=ORDER_TYPES, default='Order')
    customer_name = models.CharField('Write your full name',max_length=100, blank=True)
    customer_address = models.CharField('Write your full address', max_length=100, blank=True)
    supplier_name = models.CharField("Write supplier's full name", max_length=100, blank=True)
    supplier_address = models.CharField("Write supplier's full address", max_length=100, blank=True)
    order_date = models.DateField(auto_now=True)
    products = models.TextField("Write your order on a list")
    notes = models.TextField("Write your notes for the supplier")

    def __str__(self):
        return f'{self.order_type} - {self.supplier_name} - {self.order_date}'