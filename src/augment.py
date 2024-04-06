import pandas as pd
from src import geocode, weather

def rank_dict(df, column):
    sorted_df = df[column].value_counts().sort_values(ascending=False).reset_index()

    ranks = list(sorted_df.index + 1)
    for index, row in sorted_df.iterrows():
        if index != 0 and row['count'] == sorted_df.iloc[index - 1]['count']:
            ranks[index] = ranks[index - 1]
    
    sorted_df['rank'] = ranks
    return sorted_df.set_index(column)['rank'].to_dict()

def create_df(incident_list):
    incident_df = pd.DataFrame(incident_list, columns=['date_time', 'incident_number', 'location', 'nature', 'incident_ori'])
    incident_df.date_time = pd.to_datetime(incident_df.date_time, format="%m/%d/%Y %H:%M")

    # Weekday starting from Sunday (1)
    incident_df['Day of Week'] = incident_df.date_time.apply(lambda date: (date.weekday() + 1) % 7 + 1)

    # Hour of the date time
    incident_df['Time of Day'] = incident_df.date_time.apply(lambda datetime: datetime.hour)

    # Side of Town
    geocoder = geocode.GeoCoder()
    incident_df['latlong'] = incident_df.location.apply(geocoder.get_latlong)
    if geocoder.api_hit_count > 0:
        geocoder.update_cache()

    incident_df['Side of Town'] = incident_df.latlong.apply(geocode.side)

    # TODO Weather
    incident_df['Weather'] = weather.weather_code(incident_df)

    # Location Rank
    loc_rank = rank_dict(incident_df, 'location')
    incident_df['Location Rank'] = incident_df.location.apply(lambda loc: loc_rank[loc])

    # Incident Rank
    incident_rank = rank_dict(incident_df, 'nature')
    incident_df['Incident Rank'] = incident_df.nature.apply(lambda nature: incident_rank[nature])

    # EMSSTAT
    emsstat_dict = incident_df.groupby(['location', 'date_time'])['incident_ori'].apply(lambda x: any('EMSSTAT' == x)).to_dict()
    incident_df['loc_time'] = list(zip(incident_df.location, incident_df.date_time))
    incident_df['EMSSTAT'] = incident_df.loc_time.apply(lambda x: emsstat_dict[x])

    return incident_df[['Day of Week', 'Time of Day', 'Weather', 'Location Rank', 'Side of Town', 'Incident Rank', 'nature', 'EMSSTAT']]