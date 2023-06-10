from django.core.management.base import BaseCommand
import pandas as pd
from django.conf import settings
from products.models import Hashtag
import requests
import time

class Command(BaseCommand):
    help = 'Update hash thumbnail'

    def handle(self, *args, **options):
        endPoint = "https://zero-houst.s3.ap-northeast-2.amazonaws.com/"
        for hashQ in Hashtag.objects.all():
            hashQ.hash_thumbnail = endPoint + hashQ.room_type + "/" + str(hashQ.hash_seq) + ".png"
            hashQ.save()
            print(hashQ.hash_thumbnail)
