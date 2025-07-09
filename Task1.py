import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {
    "vs_currency": "usd",
    "days": "7",  
    "interval": "daily"
}

response = requests.get(url, params=params)
data = response.json()

prices = data['prices']  

df = pd.DataFrame(prices, columns=["Timestamp", "Price"])
df['Date'] = pd.to_datetime(df['Timestamp'], unit='ms')
df.set_index('Date', inplace=True)

plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Price'], marker='o', linestyle='-', color='blue')
plt.title("Bitcoin Price Over Last 7 Days")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.tight_layout()
plt.show()


