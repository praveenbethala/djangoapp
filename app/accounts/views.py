from django.shortcuts import render
from .models import UserProfileModel, UserCartModel

class accountuser_details():
    user = User.objects.create_user(
        username=phone_number,
        email=email,
        is_customer=is_customer,
        is_admin=is_admin,
    )
 class user_cart():   
        user_cart = UserCartModel.objects.create(
        owner=user,
        price=0,)

        users = User.objects.all()

        

