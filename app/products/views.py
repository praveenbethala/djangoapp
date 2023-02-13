from django.shortcuts import render
from .models import ProductMainModel
class product():
    product = ProductMainModel.objects.create(
        title=title,
        description=description,
        price=price,
    )
class productDatails():
   products = ProductMainModel.objects.all()
    for product in products:
        images = ProductImageModel.objects.filter(product=product)  
    product = ProductMainModel.objects.create(
        title=title,
        description=description,
        price=price,
    )
    image_1 = None  
    image_2 = None  

    ProductImageModel.objects.create(
        product=product,
        image=image_1,
    )

    ProductImageModel.objects.create(
        product=product,
        image=image_2,
    )       



