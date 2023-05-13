from django.db import models

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username
    

class AccountActivity(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    page_history = models.JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return f"Account Activity for {self.account.username}"
    
class Business(models.Model):
    id = models.AutoField(primary_key=True)
    business_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.business_name
    
class InventoryItem(models.Model):
    id = models.AutoField(primary_key=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name