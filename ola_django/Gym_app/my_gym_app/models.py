from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
 

# User registration model
class UserRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_of_birth = models.DateField()

    # def __str__(self) -> str:
    #      return (
    #         f"First Name: {self.first_name}\n"
    #         f"Last Name: {self.last_name}\n"
    #         f"Email: {self.email}\n"
    #         f"Password: {self.password}\n" # should this field be include?
    #         f"Date of Birth: {self.date_of_birth}\n"
    #     )

# Login Model
class Login(models.Model):
    e_mail = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return (
            f"Password: {self.password}\n" 
            f"Email: {self.e_mail}"
            )
    
    