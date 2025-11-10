import requests
import matplotlib.pyplot as plt

url = 'https://bank.gov.ua/NBU_Exchange/exchange_site?json&valcode=usd&start=20251103&end=20251110&sort=exchangedate&order=desc'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    dates = [record['exchangedate'] for record in data]
    rates = [record['rate'] for record in data]

    dates.reverse()
    rates.reverse()

    print("💵 Курс долара США (USD) за період 03.11.2025 — 10.11.2025:\n")
    for d, r in zip(dates, rates):
        print(f" {d}: {r:.2f} грн")

    # Побудова графіка
    plt.figure(figsize=(8, 5))
    plt.plot(dates, rates, marker='o', linestyle='-', linewidth=2)
    plt.title('Зміна курсу USD за період 03.11.2025 — 10.11.2025', fontsize=14)
    plt.xlabel('Дата', fontsize=12)
    plt.ylabel('Курс (грн)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
