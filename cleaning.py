import pandas as pd

def database(country, ranking):
    df = pd.read_csv('../data-analysis-pipeline/Input/results.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['day'] = df['date'].dt.day
    df['month'] = df['month'].dt.month
    df['year'] = df['year'].dt.year
    df = df.loc[(df['year'] > 1990)]
    coleliminar = ['date', 'city', 'country', 'neutral', 'day', 'month', 'year']
    df = df.drop(coleliminar, axis=1)

    def tournament(e):
        listtourn = ['CONCACAF Nations League', 'Gold Cup qualification', 'Oceania Nations Cup', 'Friendly', 'African Cup of Nations qualification', 'UEFA Euro', 'African Nations Championship qualifying', 'UEFA Nations League', 'African Cup of Nations', 'Copa América qualification', 'Gold Cup', 'FIFA World Cup', 'Oceania Nations Cup qualification', 'CONCACAF Nations League qualifying', 'Confederations Cup', 'UEFA Euro qualification', 'Copa América', 'FIFA World Cup qualification']
        if e in listtourn:
            return e
        else:
            return 'No vale'
    df['tournament'] = df['tournament'].apply(tournament)
    df = df.loc[(df['tournament'] != 'No vale')]

    def points(value1, value2):
        value = 0
        if value1 > value2:
            value += 3
        elif value1 == value2:
            value += 1
        elif value1 < value2:
            value == 0
        return value
    
    for index, row in df.iterrows():
        df.loc[index, 'home_points'] = points(row['home_score'], row['away_score'])

    for index, row in df.iterrows():
        df.loc[index, 'away_points'] = points(row['away_score'], row['home_score'])
    
    df = [['home_team', 'away_team', 'home_points', 'away_points']]
    return df