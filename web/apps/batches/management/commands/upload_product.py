from django.core.management.base import BaseCommand
import pandas as pd
from django.conf import settings
import requests
import time
import re

class Command(BaseCommand):
    help = 'Upload product list'

    def handle(self, *args, **options):
        csvFile = settings.BASE_DIR.parent / "batches/management/commands/seeder_products_after_error.csv"
        df = pd.read_csv(csvFile, header=0)

        endPoint = "http://127.0.0.1:8000/products/"
        for idx, row in df.iterrows():
            prodPrice = int(re.sub(r'[,원]', '', row['prod_price'].strip()))
            prodDiscount = int(re.sub(r'[,원]', '', row['prod_discount'].strip()))
            if prodPrice == 0 or prodDiscount == 0:
                prodPrice = max(prodPrice, prodDiscount)
                prodDiscount = max(prodPrice, prodDiscount)
            # print({
            #     "brand_name": row['brand_name'],
            #     "prod_price": prodPrice,
            #     "prod_discount": prodDiscount,
            #     "prod_link": row['prod_link'],
            #     "prod_thumbnail": row['prod_thumbnail'],
            # })

            response = requests.post(
                url=endPoint,
                json= {
                    "brand_name": row['brand_name'],
                    "prod_name": row['prod_name'],
                    "prod_price": prodPrice,
                    "prod_discount": prodDiscount,
                    "prod_link": row['prod_link'],
                    "prod_thumbnail": row['prod_thumbnail'],
                }
            )
            print(response)
            time.sleep(0.5)
