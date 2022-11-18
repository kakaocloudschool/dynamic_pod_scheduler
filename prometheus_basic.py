import requests
import time
from datetime import datetime
from datetime import timedelta

today = datetime.today() - timedelta(hours=1)

response = requests.get('http://192.168.50.103:9090/api/v1/query',
                       params={'query': 'http_request_duration_seconds_bucket',
                              'time':time.mktime(today.timetuple())}) 

res = response.json()['data']['result']

print(res)