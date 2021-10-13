import json
import requests
import pandas as pd

url = 'https://xd0u5m6y4r-2.algolianet.com/1/indexes/event-edition-eve-a1deadc9-75a4-41f3-8106-a249f573a88b_en-gb/query?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%203.27.1&x-algolia-application-id=XD0U5M6Y4R&x-algolia-api-key=d5cd7d4ec26134ff4a34d736a7f9ad47'


def get_payload(page):
    return {
        'params': f'query=&page={page}&facetFilters=&optionalFilters=%5B%5D'
    }


# fields to save:
# name
# companyName
# website
# phone
# email
# countryName
# mainStandHolderName

result = []
page = 0
i = 0

while True:
    r = requests.post(url, data=json.dumps(get_payload(page)), headers={'Content-Type': 'application/json'})

    data = r.json()
    hits_data = data['hits']

    if len(hits_data) == 0:
        break

    for row in hits_data:
        result.append(
            {
                'name': row['name'],
                'companyName': row['companyName'],
                'website': row['website'],
                'phone': row['phone'],
                'email': row['email'],
                'countryName': row['countryName'],
                'mainStandHolderName': row['mainStandHolderName'],
            }
        )

    i = i + 1
    page = page + 1

df = pd.DataFrame(result)
# noinspection PyTypeChecker
df.to_csv('result.csv')
