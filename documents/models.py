from django.db import models
from accounts.models import User
# Create your models here.


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    invoice_no = models.CharField(max_length=200)
    comments = models.TextField()
    description = models.CharField(max_length=200)
    status = models.NullBooleanField(default=False)
    # project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    discount = models.CharField(max_length=200)

class Receipt(models.Model):
    date = models.DateTimeField()
    receipt_no = models.CharField(max_length=200)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
