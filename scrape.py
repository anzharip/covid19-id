import requests
from lxml import html
import json
import datetime

url = 'https://www.covid19.go.id'

try:    
    pageContent = requests.get(url)
except requests.ConnectionError as e:
    print(e)
finally:
    tree = html.fromstring(pageContent.content)

indonesia_positif = tree.xpath(
    '//*[@id="post-2334"]/div/div[6]/div/div[2]/div/div[1]/p[2]/strong/text()')
indonesia_sembuh = tree.xpath(
    '//*[@id="post-2334"]/div/div[6]/div/div[2]/div/div[1]/p[3]/strong/text()')
indonesia_meninggal = tree.xpath(
    '//*[@id="post-2334"]/div/div[6]/div/div[2]/div/div[1]/p[4]/strong/text()')

global_negara_kawasan = tree.xpath(
    '//*[@id="post-2334"]/div/div[6]/div/div[1]/div/div[1]/p[2]/strong/text()')
global_kasus_terkonfirmasi = tree.xpath(
    '//*[@id="post-2334"]/div/div[6]/div/div[1]/div/div[1]/p[3]/strong/text()')
global_kematian = tree.xpath(
    '//*[@id="post-2334"]/div/div[6]/div/div[1]/div/div[1]/p[4]/strong/text()')

covid_data = {
    "Indonesia": {
        "Positif": int(indonesia_positif[0].replace(",", "")),
        "Sembuh": int(indonesia_sembuh[0].replace(",", "")),
        "Meninggal": int(indonesia_meninggal[0].replace(",", "")),
    },
    "Global": {
        "Negara/Kawasan": int(global_negara_kawasan[0].replace(",", "")),
        "Kasus Terkonfirmasi": int(global_kasus_terkonfirmasi[0].replace(",", "")),
        "Kematian": int(global_kematian[0].replace(",", "")),
    },
    "Timestamp": str(datetime.datetime.now()),
    "Source": url,

}

print('indonesia_positif: {}'.format(indonesia_positif))
print('indonesia_sembuh: {}'.format(indonesia_sembuh))
print('indonesia_meninggal: {}'.format(indonesia_meninggal))

print('global_negara_kawasan: {}'.format(global_negara_kawasan))
print('global_kasus_terkonfirmasi: {}'.format(global_kasus_terkonfirmasi))
print('global_kematian: {}'.format(global_kematian))

print('covid_data: {}'.format(covid_data))

# Write to json file
with open('covid_data.json', 'w') as outfile:
    json.dump(covid_data, outfile)