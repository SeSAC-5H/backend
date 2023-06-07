from django.core.management.base import BaseCommand
import pandas as pd
from django.conf import settings
import requests
import time

class Command(BaseCommand):
    help = 'Upload brand list'

    def handle(self, *args, **options):
        csvFile = settings.BASE_DIR.parent / "batches/management/commands/seeder_brands.csv"
        df = pd.read_csv(csvFile, header=0)

        endPoint = "http://127.0.0.1:8000/brands/"
        for idx, row in df.iterrows():
            print({
                "brand_name": row['brand_name'],
                "brand_link": row['brand_link'],
            })

            response = requests.post(
                url=endPoint,
                json= {
                    "brand_name": row['brand_name'],
                    "brand_link": row['brand_link'],
                }
            )
            print(response)
            time.sleep(0.5)
