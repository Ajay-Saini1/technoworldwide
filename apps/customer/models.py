from django.db import models
from application.custom_models import DateTimeModel
from apps.user.models import User
from django.urls import reverse


class Customer(DateTimeModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_user', null=True)
    first_name = models.CharField('Full Name', max_length=30, blank=True)
    phone_number = models.BigIntegerField(blank=True, null=True, unique=True)
    
    def __str__(self):
        return self.user.first_name

    def delete(self, using=None):
        if self.user:
            self.user.delete()
        super(Customer, self).delete(using)


class CustomerAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)  # Correct field name
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer.user.username} - {self.address_line1}, {self.city}"

#    def get_absolute_url(self):
#        return reverse('edit_address', kwargs={'pk': self.pk})
