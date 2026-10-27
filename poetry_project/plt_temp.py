import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import random

def transform_data(hours, temps):
    df = pd.DataFrame({"time": pd.to_datetime(hours), "temperature_c": temps})
    df = df.sort_values("time").reset_index(drop=True)
    return df

def main():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": 55.75, "longitude": 37.61, "hourly": "temperature_2m"}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        hours = data["hourly"]["time"][:24]
        temps = data["hourly"]["temperature_2m"][:24]
        print("Данные успешно получены с API.")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        print("Используются тестовые данные.")
        base_time = datetime.datetime.now()
        hours = [(base_time + datetime.timedelta(hours=i)).isoformat() for i in range(24)]
        temps = [15.0 + (i % 5) + random.uniform(-1.5, 1.5) for i in range(24)]

    df = transform_data(hours, temps)
    
    df.to_csv("temperature_24h.csv", index=False)
    print("Сохранено в temperature_24h.csv")
    
    plt.plot(df["time"], df["temperature_c"], marker="o")
    plt.xticks(rotation=45)
    plt.title("Температура в Москве (24 часа)")
    plt.xlabel("Время")
    plt.ylabel("°C")
    plt.tight_layout()
    
    plt.savefig("temperature_24h.png")
    print("Сохранено в temperature_24h.png")

if __name__ == "__main__":
    main()