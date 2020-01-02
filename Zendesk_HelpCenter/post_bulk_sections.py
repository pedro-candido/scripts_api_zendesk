import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth
import json

# pprint(r.json())
section = [
{
    "section":
    {
        'locale': 'pt-br',
        'name': 'Seção 1',
        'description': '....'
    }
},
{
    "section":
    {
        'locale': 'pt-br',
        'name': 'Seção 2',
        'description': '....',
    }
},
]

for x in section:
    postSections = requests.post('https://{subdominium}.zendesk.com/api/v2/help_center/categories/{id}/sections.json', json=x, auth=('login','senha'))
    pprint(postSections.content)
    input()





