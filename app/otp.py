from django.core.mail import send_mail
from .models import UserLoginOtpModel

class otpLogin():
    UserLoginOtpModel.objects.create(
        owner=owner,
        otp=otp,
        active=active,)
