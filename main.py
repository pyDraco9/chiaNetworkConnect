import json
import os
import traceback
from time import sleep

import requests

chia_command = 'C:\\Users\\yourname\\AppData\\Local\\chia-blockchain\\app-1.1.5\\resources\\app.asar.unpacked\\daemon\\chia.exe show -a'


def get_nodes():
    try:
        res = requests.get('https://chia.powerlayout.com/nodes?block_height=false')
        if res.status_code == 200:
            return json.loads(res.content.decode('UTF-8'))
    except:
        traceback.print_exc()


if __name__ == '__main__':
    while True:
        nodes = get_nodes()
        for node in nodes['nodes']:
            ret = os.system(chia_command + node)
        sleep(60 * 5)
