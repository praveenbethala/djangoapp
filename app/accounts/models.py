from django.db import models
from django.contrib.auth.models import User
class  User_Model(models.Models):
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=10)
    is_customer = models.BooleanField()
    is_admin = models.BooleanField()

class userProfileModel(s.Models):
    owner=models.OneToOneField(max_length=10)
	Name=models.CharField(max_length=100)
	Date_of_birth=models.DateField()
	Gender:(
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),)
    gender = models.IntegerField(choices=GENDER_CHOICES)
	Image=models.ImageField(upload_to='accounts/images/')

 class userloginotpMode(models.Models):
    owner=models.ForeignKey(User)
    Otp=models.integerField(max_length=100)
    active=models.BooleanField()

 class UserCartProductModel():
    owner=models.ForeignKey(User)
	product=models.ForeignKey(productMainModel)
	status=(
    (0, 'COMPLETE'),
    (1, 'PENDING'),
    )
    status= models.IntegerField(choices=status_CHOICES)
   

class UserCartModel():
    owner=models.OneToOneField(max_length=10)
	products=models.MnayToManyField(max_length=10)
	price=models.IntegerField()




   

