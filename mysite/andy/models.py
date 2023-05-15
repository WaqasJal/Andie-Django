from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from .manager import MyUserManager

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255,unique=True,)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [full_name, phone_number]

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True,)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager() #new

# class Account(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=30, unique=True)
#     password = models.CharField(max_length=128)
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15)

#     class Meta:
#         app_label = 'apfelschuss.votes'
#     def __str__(self):
#         return self.username
    

# class AccountActivity(models.Model):
#     id = models.AutoField(primary_key=True)
#     account = models.ForeignKey(Account, on_delete=models.CASCADE)
#     page_history = models.JSONField(default=list, blank=True, null=True)

#     def __str__(self):
#         return f"Account Activity for {self.account.username}"
    
# class Business(models.Model):
#     id = models.AutoField(primary_key=True)
#     business_name = models.CharField(max_length=100)
#     category = models.CharField(max_length=50)
#     location = models.CharField(max_length=100, blank=True, null=True)
#     phone_number = models.CharField(max_length=15)

#     def __str__(self):
#         return self.business_name
    
# class InventoryItem(models.Model):
#     id = models.AutoField(primary_key=True)
#     business = models.ForeignKey(Business, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     category = models.CharField(max_length=50)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return self.name