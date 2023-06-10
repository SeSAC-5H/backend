from django.core.management.base import BaseCommand
import pandas as pd
from django.conf import settings
import requests
import time
import re


class Command(BaseCommand):
    help = "Upload product-hashtag list"

    def handle(self, *args, **options):
        csvFile = (
            settings.BASE_DIR.parent
            / "batches/management/commands/seeder_product_hashtags.csv"
        )
        df = pd.read_csv(csvFile, header=0)

        endPoint = "http://127.0.0.1:8000/products/hashtags/"

        respResults = [201 for _ in range(len(df))]
        for idx, row in df.iterrows():
            response = requests.post(
                url=endPoint,
                json={
                    "prod_name": row["prod_name"],
                    "hash_name": row["hash_name"],
                },
            )
            print(idx)
            respResults[idx] = response.status_code
            # if idx > 10:
            #     break
            # print(response)
            time.sleep(0.5)

        df["res"] = respResults
        # print(df)

        df.to_csv("result-product-hash.csv", index=False)
