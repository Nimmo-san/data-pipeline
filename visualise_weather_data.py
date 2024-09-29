import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def get_weather_data():
    conn = sqlite3.connect('weather_data.db')
    query  = 'SELECT * FROM weather'
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def visualise_data():
    df = get_weather_data()
    
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    city_name = "London"
    city_data = df[df['city'] == city_name]
    
    # Line plot for temperature over time
    plt.figure(figsize=(10, 5))
    plt.plot(city_data['timestamp'], city_data['temperature'], marker='o')
    plt.title(f'Temperature Over Time in {city_name}')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()
    
    # Correlation heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap of Weather Parameters")
    plt.show()
    
    # Interactive plotly visualisation
    fig = px.line(df, x='timestamp', y='temperature', color='city',
                  title='Temperature Over Time by City')
    fig.show()

if __name__ == "__main__":
    visualise_data()

