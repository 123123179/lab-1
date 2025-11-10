import requests

url = 'https://bank.gov.ua/NBU_Exchange/exchange_site?json&valcode=usd&start=20251103&end=20251110&sort=exchangedate&order=desc'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("💵 Курс долара США (USD) за період 03.11.2025 — 10.11.2025:\n")
    for record in data:
        date = record['exchangedate']
        rate = record['rate']
        print(f"📅 {date}: {rate:.2f} грн")
