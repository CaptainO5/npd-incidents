import openmeteo_requests
import numpy as np
from src import config

def distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def weather_code(df):
    date = df['date_time'].iloc[0].strftime("%Y-%m-%d")
    df_latlong = df[['latlong', 'Side of Town']].drop_duplicates()

    openmeteo = openmeteo_requests.Client()

    url = "https://archive-api.open-meteo.com/v1/archive"

    select_locs = [config.CENTER]
    for _, grp in df_latlong.groupby('Side of Town'):
        select_locs.extend(np.random.choice(grp['latlong'], 2))

    weather_codes = {}
    for loc in select_locs:
        params = {
            "latitude": loc[0],
            "longitude": loc[1],
            "start_date": date,
            "end_date": date,
            "hourly": "weather_code",
            "timezone": "America/New_York"
        }
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]
        response_loc = response.Latitude(), response.Longitude()

        hourly = response.Hourly()
        hourly_weather_code = hourly.Variables(0).ValuesAsNumpy()
        weather_codes[response_loc] = hourly_weather_code
    
    weathers = []
    for idx, row in df.iterrows():
        shortest_d = np.inf
        nearest_p = ()
        for point in weather_codes:
            d = distance(row['latlong'], point)
            if d < shortest_d:
               shortest_d = d
               nearest_p = point
         
        weathers.append(int(weather_codes[nearest_p][row['Time of Day']]))

    return weathers