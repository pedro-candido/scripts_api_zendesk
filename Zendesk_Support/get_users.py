import requests
import json
from pprint import pprint
from requests.auth import HTTPBasicAuth
from pandas import DataFrame

user = 'user'
password = 'password'

x = requests.get('https://{subdominium}.zendesk.com/api/v2/users.json', auth=(user, password))
x = x.json()

x = DataFrame(x)


x.to_csv('new_x.csv')
x.to_json('new_x.json')