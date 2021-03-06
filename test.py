import requests
import hashlib
import os
import sys
# from rauth import OAuth2Service
from pprint import pprint
from datetime import datetime, timedelta




class WAKATIME:

    prefix = "https://wakatime.com/api/v1/"
    private_key = "4661d281-417d-4f74-a811-00264d42dc39"

    def __init__(self):
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

