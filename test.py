import requests
import hashlib
import os
import sys
# from rauth import OAuth2Service
from pprint import pprint
from datetime import datetime, timedelta
import yaml
import os


class WAKATIME:

    prefix = ""
    private_key = ""

    def __init__(self, cfg_path='config.yml'):
        if not os.path.exists(cfg_path):
            private_key = input('在此处粘贴你的 api-key: ')
            config = yaml.safe_load(open(cfg_path))
        else:
            config = yaml.safe_load(open(cfg_path))

        pass


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

