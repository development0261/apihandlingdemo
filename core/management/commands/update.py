from django.core.management.base import BaseCommand
from core.models import APIDATA
import requests
import datetime
import pytz


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(
            "https://61c6effa9031850017547293.mockapi.io/api/v2/iotmock"
        )
        for i in response.json():
            old_values = APIDATA.objects.filter(
                timestamp=datetime.datetime.strptime(i["timestamp"], "%m/%d/%Y"),
                ip_address=i["ip_address"],
            )
            if not old_values:
                staff_obj = APIDATA(
                    site_name=i["site_name"],
                    latitude=i["latitude"],
                    longitude=i["longitude"],
                    datastream=i["datastream"],
                    ip_address=i["ip_address"],
                    timestamp=datetime.datetime.strptime(i["timestamp"], "%m/%d/%Y"),
                )
                staff_obj.save()

        print("update Complete")
