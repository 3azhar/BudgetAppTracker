from django.db import models

# Create your models here.

class Transaction(models.Model):
    #Transaction user wants to record( after make any changes to this* must run makemigrations cmd)
    TransactionType = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #Return a string reprensentation of model (method)
        return str(self.TransactionType)
    

class Entry(models.Model):
    transactions = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    merchant = models.CharField(max_length=200)
    description = models.TextField()
    transaction_amount = models.FloatField(max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        return str(self.merchant)

