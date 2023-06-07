from django.core.management.base import BaseCommand
import pandas as pd
from django.conf import settings
import requests
import time

class Command(BaseCommand):
    help = 'Upload hashtag list'

    def handle(self, *args, **options):
        csvFile = settings.BASE_DIR.parent / "batches/management/commands/seeder_hashtags.csv"
        df = pd.read_csv(csvFile, header=0)

        endPoint = "http://127.0.0.1:8000/hashtags/"
        for idx, row in df.iterrows():
            print({
                "hash_name": row['hash_name'],
                "room_type": row['room_type'],
            })

            response = requests.post(
                url=endPoint,
                json= {
                    "hash_name": row['hash_name'],
                    "room_type": row['room_type'],
                }
            )
            print(response)
            time.sleep(0.5)
