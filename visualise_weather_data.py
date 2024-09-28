import sqlite3
import pandas as pd


def get_weather_data():
    conn = sqlite3.connect('weather_data.db')
    query  = 'SELECT * FROM weather'
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

