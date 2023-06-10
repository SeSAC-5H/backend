from django.db import models
from core.models import BaseModel

# Create your models here.


class SubCategories(BaseModel):
    subcate_seq = models.AutoField(primary_key=True)
    subcate_name = models.CharField(default="-", max_length=100, null=False)

    class Meta:
        managed = True
        db_table = "subCategories"


class Stores(BaseModel):
    store_seq = models.AutoField(primary_key=True)
    store_name = models.CharField(default="-", max_length=100, null=False)
    store_id = models.CharField(default="-", max_length=100, null=False)
    store_subcate = models.ForeignKey(
        to="stores.SubCategories",
        db_column="subcate_seq",
        on_delete=models.PROTECT,
    )
    store_time = models.CharField(default="-", max_length=300, null=False)
    store_address_old = models.CharField(
        default="-", max_length=300, null=False
    )
    store_address_new = models.CharField(
        default="-", max_length=300, null=False
    )
    store_tel = models.CharField(default="-", max_length=100, null=False)
    store_link = models.CharField(default="-", max_length=300, null=False)
    store_coord_x = models.FloatField(default=0, null=False)
    store_coord_y = models.FloatField(default=0, null=False)

    class Meta:
        managed = True
        db_table = "stores"
