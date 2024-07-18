class DailyWeather:
    def __init__(self, date, temperature, humidity, wind_speed):
        self.__date = date
        self.__temperature = temperature
        self.__humidity = humidity
        self.__wind_speed = wind_speed

    # Métodos para obtener y establecer atributos (encapsulamiento)
    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature

    def get_humidity(self):
        return self.__humidity

    def set_humidity(self, humidity):
        self.__humidity = humidity

    def get_wind_speed(self):
        return self.__wind_speed

    def set_wind_speed(self, wind_speed):
        self.__wind_speed = wind_speed


class WeeklyWeather:
    def __init__(self):
        self.__daily_weather_list = []

    def add_daily_weather(self, daily_weather):
        self.__daily_weather_list.append(daily_weather)

    def calculate_weekly_average(self):
        total_temp = 0
        total_humidity = 0
        total_wind_speed = 0
        days = len(self.__daily_weather_list)

        if days == 0:
            return None  # Manejo del caso donde no hay datos

        for daily_weather in self.__daily_weather_list:
            total_temp += daily_weather.get_temperature()
            total_humidity += daily_weather.get_humidity()
            total_wind_speed += daily_weather.get_wind_speed()

        avg_temp = total_temp / days
        avg_humidity = total_humidity / days
        avg_wind_speed = total_wind_speed / days

        return {
            'average_temperature': avg_temp,
            'average_humidity': avg_humidity,
            'average_wind_speed': avg_wind_speed
        }

# Ejemplo de uso
if __name__ == "__main__":
    day1 = DailyWeather("2024-07-01", 25, 60, 15)
    day2 = DailyWeather("2024-07-02", 27, 65, 10)
    day3 = DailyWeather("2024-07-03", 26, 70, 20)
    day4 = DailyWeather("2024-07-04", 28, 55, 12)
    day5 = DailyWeather("2024-07-05", 30, 50, 8)
    day6 = DailyWeather("2024-07-06", 29, 60, 10)
    day7 = DailyWeather("2024-07-07", 31, 55, 14)

    weekly_weather = WeeklyWeather()
    weekly_weather.add_daily_weather(day1)
    weekly_weather.add_daily_weather(day2)
    weekly_weather.add_daily_weather(day3)
    weekly_weather.add_daily_weather(day4)
    weekly_weather.add_daily_weather(day5)
    weekly_weather.add_daily_weather(day6)
    weekly_weather.add_daily_weather(day7)

    averages = weekly_weather.calculate_weekly_average()
    print("Promedio semanal:")
    print(f"Temperatura: {averages['average_temperature']}°C")
    print(f"Humedad: {averages['average_humidity']}%")
    print(f"Velocidad del viento: {averages['average_wind_speed']} km/h")
