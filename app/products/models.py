from django.db import models
class productMainModel():
    	Title=models.CharField(max_length=100)
		Description=models.CharField(max_length=100)
		Unique_id=models.IntegerField()
		Price=models.IntegerField()

class productImageModel():
    product:models.ForeignKey(User)(productMainModel)
