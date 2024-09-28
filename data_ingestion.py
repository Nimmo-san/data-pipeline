import schedule
import time
import requests
import sqlite3
import logging
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    # can also be added to a file named etl_process.log
    filename=None,
    level=logging.INFO,  # Set level to INFO or DEBUG to capture more details
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format for the logs
)

# Example log message
logging.info("Logger has been configured successfully.")


def extract_weather_data(city):
    """"""
    try:
        logging.info(f"Starting data extraction for city: {city}")
        api_key = os.getenv("WEATHER_API_KEY")
        if not api_key:
            raise ValueError("API key not found in environment variables.")
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        logging.info(f"Data successfully extracted for city: {city}")
        return response.json()
    except Exception as e:
        logging.error(f"Failed to extract data for city: {city} - Error: {e}")
        return None	


def transform_weather_data(raw_data):
    try:
        logging.info("Starting data transformation.")
        if raw_data:
            transformed_data = {
                "city": raw_data["name"],
                "temperature": raw_data["main"]["temp"],
                "humidity": raw_data["main"]["humidity"],
                "description": raw_data["weather"][0]["description"],
                "timestamp": raw_data["dt"]
            }
            logging.info(f"Data transformation completed for city: {transformed_data['city']}")
            return transformed_data
        else:
            logging.warning("No raw data to transform.")
            return None
    except KeyError as e:
        logging.error(f"Data transformation error - Missing key: {e}")
        return None


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
    try:
        logging.info(f"Starting data load for city: {data['city']}")
        conn = sqlite3.connect("weather_data.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
                            city TEXT, 
                            temperature REAL, 
                            humidity INTEGER, 
                            description TEXT, 
                            timestamp INTEGER)''')
        cursor.execute('''INSERT INTO weather (city, temperature, humidity, description, timestamp) 
                          VALUES (?, ?, ?, ?, ?)''', 
                       (data["city"], data["temperature"], data["humidity"], data["description"], data["timestamp"]))
        conn.commit()
        conn.close()
        logging.info(f"Data successfully loaded for city: {data['city']}")
    except Exception as e:
        logging.error(f"Failed to load data for city: {data.get('city', 'Unknown')} - Error: {e}")


def run_etl(cities: list):
        calls_made = 0
        max_calls_per_hours = 60
        delay = 3600 / max_calls_per_hours
        logging.info("ETL process started.")
        for city in cities:
                raw_data = extract_weather_data(city)
                if not raw_data:
                        logging.error(f"Skipping transformation and loading for city: {city} due to extraction failure.")
                
                transformed_data = transform_weather_data(raw_data=raw_data)
                if not transformed_data:
                        logging.error(f"Skipping loading for city: {city} due to transformation failure.")
                
                load_weather_data(transformed_data)

                calls_made += 1
                if calls_made < max_calls_per_hours:
                        time.sleep(delay)
                else:
                    time.sleep(3600)
                    calls_made = 0
        logging.info("ETL process complete.")
        
    





if __name__ == '__main__':
	# Scheduling to run ETL every hour
	schedule.every(1).hour.do(run_etl, cities=["London", "Manchester", "New York"])

	while True:
		schedule.run_pending()
		time.sleep(1)