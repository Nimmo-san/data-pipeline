from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import sqlite3
import pandas as pd


app = FastAPI()


# adding a cors middleware 
# very useful for development but has to be restricted for production

app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

def get_weather_data_from_db():
    """
    
    """
    conn = sqlite3.connect('weather_data.db')
    query = "SELECT * FROM weather"
    df = pd.read_sql_query(query, conn)
    conn.close()
    print(df.head())
    return df

@app.get("/")
def read_root():
    return {'message': 'Welcome to my Weather Data API!!'}


@app.get("/cities", response_model=List[str])
def get_cities():
    """ """
    df = get_weather_data_from_db()
    return df['city'].unique().tolist()


@app.get("/weather/{city}")
def get_weather(city: str):
    """ """
    df = get_weather_data_from_db()
    city_data = df[df['city'].str.lower() == city.lower()]
    if city_data.empty:
        return {"error": f"No data found for city '{city}'"}
    
    return city_data.to_dict(orient="records")