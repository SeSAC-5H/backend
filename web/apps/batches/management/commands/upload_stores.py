from django.core.management.base import BaseCommand
import pandas as pd
from django.conf import settings
import requests
import time


class Command(BaseCommand):
    help = "Upload store list"

    def handle(self, *args, **options):
        csvFile = (
            settings.BASE_DIR.parent
            / "batches/management/commands/seeder_stores_detail.csv"
        )
        df = pd.read_csv(csvFile, header=0)
        df = df.fillna("-")

        endPoint = "http://127.0.0.1:8000/stores/"
        for idx, row in df.iterrows():
            response = requests.post(
                url=endPoint,
                json={
                    "store_name": row["COT_CONTS_NAME"],
                    "store_id": row["COT_CONTS_ID"],
                    "store_subcate": row["COT_THEME_SUB_ID"],
                    "store_time": row["COT_VALUE_03"],
                    "store_address_old": row["COT_ADDR_FULL_OLD"],
                    "store_address_new": row["COT_ADDR_FULL_NEW"],
                    "store_tel": row["COT_TEL_NO"],
                    "store_link": row["COT_EXTRA_DATA_02"],
                    "store_coord_x": row["COT_COORD_X"],
                    "store_coord_y": row["COT_COORD_Y"],
                    "store_insta": row["COT_VALUE_05"],
                    "store_item": row["COT_VALUE_04"],
                },
            )
            print(response)
            time.sleep(0.5)
