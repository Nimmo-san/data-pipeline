import schedule
import time
import requests
import sqlite3
from pprint import pprint


def extract_weather_data(city):
	api_key = "2bce98f4eae16b83917e8a2b32ea8ea1"
	try:
		url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
		response = requests.get(url)
		return response.json()
	except Exception as e:
		print(e)	


def transform_weather_data(raw_data):
    transformed_data = {
        "city": raw_data["name"],
        "temperature": raw_data["main"]["temp"],
        "humidity": raw_data["main"]["humidity"],
        "description": raw_data["weather"][0]["description"],
        "timestamp": raw_data["dt"]
    }
    return transformed_data


def create_database():
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
                      city TEXT, 
                      temperature REAL, 
                      humidity INTEGER, 
                      description TEXT, 
                      timestamp INTEGER)''')
    conn.commit()
    conn.close()

def load_weather_data(data):
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO weather (city, temperature, humidity, description, timestamp) 
                      VALUES (?, ?, ?, ?, ?)''', 
                   (data["city"], data["temperature"], data["humidity"], data["description"], data["timestamp"]))
    conn.commit()
    conn.close()

def run_etl(cities):
	calls_made = 0
	max_calls_per_hour = 60
	delay = 3600 / max_calls_per_hour	
	for city in cities:

		raw_data = extract_weather_data(city)
		transformed_data = transform_weather_data(raw_data)
		load_weather_data(transformed_data)

		calls_made += 1
		if calls_made < max_calls_per_hour:
			time.sleep(delay)
		else:
			time.sleep(3600)
			calls_made = 0

if __name__ == '__main__':
	# Scheduling to run ETL every hour
	schedule.every(1).hour.do(run_etl, cities=["London", "Manchester", "New York"])

	while True:
		schedule.run_pending()
		time.sleep(1)