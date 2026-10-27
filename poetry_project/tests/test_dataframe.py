from plt_temp import transform_data

def test_transform_data():
    # Локальные тестовые данные (время намеренно перепутано, дабы проверить сортировку)
    hours = ["2023-10-27T15:00", "2023-10-27T12:00", "2023-10-27T14:00"]
    temps = [10.5, 8.0, 9.5]
    
    df = transform_data(hours, temps)
    
    #Проверка названий столбцов
    assert list(df.columns) == ["time", "temperature_c"], "Неверные названия столбцов"
    
    #Проверка количества строк
    assert len(df) == 3, "Неверное количество строк"
    
    #Проверка сортировки строк по времени
    assert df["time"].is_monotonic_increasing, "Данные не отсортированы по времени"
    
    #Проверка соответствия температуры времени после сортировки
    assert df.iloc[0]["temperature_c"] == 8.0, "Неверная температура для 12:00"
    assert df.iloc[1]["temperature_c"] == 9.5, "Неверная температура для 14:00"
    assert df.iloc[2]["temperature_c"] == 10.5, "Неверная температура для 15:00"