from django.db import models
from core.models import BaseModel

# Create your models here.
STORE_TYPE_CHOICES = (
    ("1", "카페"),
    ("2", "식당"),
    ("3", "리필샵"),
    ("4", "생필품"),
    ("5", "기타"),
)


class Stores(BaseModel):
    store_seq = models.AutoField(primary_key=True)
    store_name = models.CharField(default="-", max_length=100, null=False)
    store_id = models.CharField(default="-", max_length=100, null=False)
    store_subcate = models.CharField(
        default="-", max_length=50, choices=STORE_TYPE_CHOICES, null=False
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
    store_coord_x = models.CharField(default="-", max_length=100, null=False)
    store_coord_y = models.CharField(default="-", max_length=100, null=False)
    store_insta = models.CharField(default="-", max_length=300, null=False)
    store_item = models.CharField(default="-", max_length=300, null=False)

    class Meta:
        managed = True
        db_table = "stores"
