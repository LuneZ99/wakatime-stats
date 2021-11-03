import requests
from pprint import pprint
from datetime import datetime, timedelta
import yaml
import os
import sys
import shutil


class WAKATIME:

    prefix = "https://wakatime.com/api/v1/"
    private_key = ""


    def __init__(self, private_key):
        self.private_key = private_key



    def get(self):

        url = self.prefix+'users/current/durations'
        params = {
            'date': datetime.today() - timedelta(days=1),
            # 'unreleased': True,
            # 'start': datetime.today(),
            # 'end': datetime.today(),
            'api_key': self.private_key,
            'slice_by': "entity"
        }
        resp = requests.get(url, params=params)
        print(resp.status_code)
        pprint(resp.json())


if __name__ == '__main__':
    w = WAKATIME()
    print(datetime.today())
    pass

