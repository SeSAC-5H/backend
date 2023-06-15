from django.db import models
from core.models import BaseModel

# Create your models here.

class Product(BaseModel):
    prod_seq = models.AutoField(primary_key=True)
    prod_name = models.CharField(default="-", max_length=100, null=False)
    prod_link = models.CharField(default="-", max_length=300, null=False)
    prod_price = models.IntegerField(default=0, null=False)
    prod_discount = models.IntegerField(default=0, null=False)
    prod_thumbnail = models.CharField(default="-", max_length=300, null=False)

    brand_seq = models.ForeignKey(to="products.Brand", db_column="brand_seq", on_delete=models.PROTECT)

    def get_brand_name(self):
        return self.brand_seq.brand_name

    class Meta:
        managed = False
        db_table = 'products'

class Brand(BaseModel):
    brand_seq = models.AutoField(primary_key=True)
    brand_name = models.CharField(default="-", max_length=100, null=False)
    brand_link = models.CharField(default="-", max_length=300, null=False)

    class Meta:
        managed = False
        db_table = 'brands'

class Hashtag(BaseModel):
    hash_seq = models.AutoField(primary_key=True)
    hash_name = models.CharField(default="-", max_length=100, null=False)
    hash_avg_price = models.IntegerField(default=0,)
    room_type = models.CharField(default="-", max_length=4, null=False)
    hash_desc = models.CharField(default="-", max_length=1000, null=False)
    hash_thumbnail = models.CharField(default="-", max_length=300, null=False)
    is_active = models.CharField(default="Y", max_length=1, null=False)

    class Meta:
        managed = False
        db_table = 'hashtags'

class ProductHashtag(BaseModel):
    prod_hash_seq = models.AutoField(primary_key=True)

    prod_seq = models.ForeignKey(to="products.Product", db_column="prod_seq", on_delete=models.PROTECT)
    hash_seq = models.ForeignKey(to="products.Hashtag", db_column="hash_seq", on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'productHashtags'