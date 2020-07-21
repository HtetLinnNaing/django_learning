from django.db import models
from shop import categories, apps


# Create your models here.
class inventory(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.CharField(choices=categories.CATEGORY, max_length=3)
    label = models.CharField(choices=categories.LABEL, max_length=2)
    item_image = models.ImageField(upload_to=apps.ShopConfig.name + "/images/")
    description = models.TextField(max_length=1000, null=True)
    item_quantity = models.IntegerField(default=1)
    unit_price = models.CharField(choices=categories.PRICE_UNIT, max_length=2)

    def __str__(self):
        return self.item_name

    class Meta:
        db_table = "inventory"
