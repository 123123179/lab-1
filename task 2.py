import requests

my_response = requests.get('https://bank.gov.ua/NBU_Exchange/exchange_site?json&valcode=usd&start=20251103&end=20251110&sort=exchangedate&order=desc')

print(my_response.json())
print(my_response)