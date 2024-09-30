# Weather Data ETL & Visualisation Project

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup & Installation](#setup--installation)
- [Database Schema](#database-schema)
- [ETL Pipeline](#etl-pipeline)
- [Data Visualisation](#data-visualisation)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [Acknowledgements](#acknowledgements)

---

## Overview
This project is a simple ETL (Extract, Transform, Load) pipeline that collects weather data from an external API, stores it in a SQLite database, and visualises it using Python libraries.

The pipeline collects weather parameters like temperature, pressure, humidity, and wind data from multiple cities, and stores them for historical analysis and visualisation.

---

## Project Structure

- **Root Files**:
  - `README.md`: A description of the project.
  - `data_ingestion.py`: Main extraction of the data.
  - `visualise_weather_data.py`: Visualising of the data.
  - `weather_api.py`: Local api for my testing of index.html
  - `index.html`: Simple web page to visualise the data from the api.
  - `.gitignore`: Specifies files that should be ignored by Git.
  - `requirements.txt` or `Pipfile`: Dependencies needed for the project.

---

## Technologies Used

- **Python**: Main programming language for ETL and visualisation.
- **SQLite**: Lightweight database for storing weather data.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib, Seaborn, Plotly**: Libraries for data visualisation.
- **Requests**: For making HTTP requests to the weather API.
- **FastAPI**: For making local calls to visualise data.

---

## Setup & Installation

### Prerequisites
- Python 3.x installed on your system.
- Access to the weather API (e.g., [OpenWeatherMap](https://openweathermap.org/)).

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd project-folder
2. **Install Required Packages**
    ```bash
    pip install -r requirements.txt
3. **Set up Environment Variable by creating a .env**
    ```bash
    WEATHER_API_KEY=your_api_key_here
4. **Execute the data_ingestion.py script to start collecting data**
    ```bash
    python data_ingestion.py

### Using a More Structured Input Format
Configure the List of Cities
To specify the cities for which to gather weather data, create a `cities.csv` file in the root of the project directory. Each line should contain a city name. For example:
- **CSV Format**: Create a `cities.csv` file with the following structure:
    ```csv
    city,country
    New York,US
    London,UK
    Paris,FR
    ```
Or if you rather use json file
- **JSON Format**: Create a `cities.json` file with the following structure:
    ```json
    [
        {"city": "New York", "country": "US"},
        {"city": "London", "country": "UK"}
    ]
    ```

## DataBase Schema 
Weather data is stored in SQLite database under the name of weather_data.db
- Below is the schema of the weather table

### ADD SCHEMA

### ETL Pipeline

1. **Extracting** weather data from a weather API (e.g. OpenWeatherMap).
2. **Transforming** the raw JSON data into structured format suitable for storage.
3. **Loading** the transformed data into the weather_data.db SQLite database.

### ETL Code snippet
```python
    import requests
    import sqlite3

    def extract_weather_data(city):
        # Code to extract data from API using requests
        pass

    def transform_weather_data(raw_data):
        # Code to transform JSON data
        pass

    def create_database():
        # Code to create DB using sqlite3
        pass

    def load_weather_data(data):
        # Code to insert data into SQLite database
        pass
```
    
### How to use 

1. Ensuring the .env has the correct API key
2. Run the script
```bash
    python data_ingestion.py
```
    
Logs of the process are stored in etl_process.log

## Data Visualisation
The script ```visualise_weather_data.py``` script is responsible for accessing and visualising the data stored in the SQLite DB.
Using ```Pandas``` to manipulate the data and ```MatplotLib```, ```Seaborn```, and ```plotly``` to create simple visualisations.

### Example
1. **Temperature Over Time**: Line plots of temperature over time for different cities.

### Visualisation Code snippet
```python
    import matplotlib.pyplot as plt
    import pandas as pd

    def get_weather_data():
        # Load data from SQLite database
        pass 

    def visualize_data():
        # Create simple plots for weather data
        pass
```

### How to use 

After running ```data_ingestion.py``` script to gather the latest data, run the script
```bash
    python visualise_weather_data.py
```

## Usage


## Future Improvements

- **Add more data sources** Example weather forecasts, etc. 
- **ETL Process is too slow?** Using parallelisation and batching to improve speed and efficiency.
- **Better data quality?** Implementing data validation and alert system as to catch data issues early.
- **Need analysis and reporting?** Implementing aggregation and reporting to create summarised views of the data.
- **Improve data visualisations** Providing a more comprehensive data visualisations.

---

<!--### **Notes on the README Content**-->
