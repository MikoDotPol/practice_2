import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import random

url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 55.75, "longitude": 37.61, "hourly": "temperature_2m"}

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    print("успешное соединение через API")
    hours = data["hourly"]["time"][:24]
    temps = data["hourly"]["temperature_2m"][:24]
except requests.exceptions.RequestException as e:
    print(f"Не удалось подключиться к API ({e}), генерируем данные для продолжения практики")
    base_time = datetime.datetime.now()
    hours = [(base_time + datetime.timedelta(hours=i)).isoformat() for i in range(24)]
    temps = [20.0 + (i%5) + random.uniform(-3, 3) for i in range(24)]

df = pd.DataFrame({"time": pd.to_datetime(hours), "temperature_c": temps})
df = df.sort_values("time").reset_index(drop=True)
df.to_csv("temperature_24h.csv", index=False)
print("Сохранено в temperature_24h.csv")

plt.plot(hours, temps, marker="o")
plt.xticks(rotation=45)
plt.title("Температура в Москве (24 часа)")
plt.xlabel("Время")
plt.ylabel("°C")
plt.tight_layout()
plt.show()
