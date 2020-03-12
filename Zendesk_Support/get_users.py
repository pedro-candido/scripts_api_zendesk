import requests
import json
from pprint import pprint
from requests.auth import HTTPBasicAuth
import pandas as pd
# import csv

user = 'Email'
password = 'Senha'
base_url = 'https://{subdominio}.zendesk.com/api/v2/users.json?page='

all_users = []
filtered_users = []

for i in range(0,250):
    url = base_url+str(i)
    response = requests.get(url, auth=(user, password)).json()
    users = response.get('users')
    all_users += users
    print(url)


for user in all_users:
    if(user['role'] == 'end-user'):
        filtered_users.append(user['email'])

filtered_users = pd.DataFrame(filtered_users)

with pd.ExcelWriter('email_request.xlsx') as writer:
    filtered_users.to_excel(writer, sheet_name="email_request")