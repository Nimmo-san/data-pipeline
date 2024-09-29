# Weather Data ETL & Visualization Project

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
This project is an ETL (Extract, Transform, Load) pipeline that collects weather data from an external API, stores it in a SQLite database, and visualizes it using Python libraries.

The pipeline collects weather parameters like temperature, pressure, humidity, and wind data from multiple cities, and stores them for historical analysis and visualization.

---

## Project Structure


---

## Technologies Used

- **Python**: Main programming language for ETL and visualization.
- **SQLite**: Lightweight database for storing weather data.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib, Seaborn, Plotly**: Libraries for data visualization.
- **Requests**: For making HTTP requests to the weather API.

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

### ETL Pipeline

### ETL Code snippet

### How to use 

## Data Visualisation

### Visualisation Code snippet

### How to use 

## Usage

## Future Improvements

---

### **Notes on the README Content**
