import pandas as pd

def tournament(e):
    listtourn = ['CONCACAF Nations League', 'Gold Cup qualification', 'Oceania Nations Cup', 'Friendly', 'African Cup of Nations qualification', 'UEFA Euro', 'African Nations Championship qualifying', 'UEFA Nations League', 'African Cup of Nations', 'Copa América qualification', 'Gold Cup', 'FIFA World Cup', 'Oceania Nations Cup qualification', 'CONCACAF Nations League qualifying', 'Confederations Cup', 'UEFA Euro qualification', 'Copa América', 'FIFA World Cup qualification']
    if e in listtourn:
        return e
    else:
        return 'No vale'

def points(value1, value2):
    value = 0
    if value1 > value2:
        value += 3
    elif value1 == value2:
        value += 1
    elif value1 < value2:
        value == 0
    return value

def database(c1, c2):
    df = pd.read_csv('../data-analysis-pipeline/Input/results.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df = df.loc[(df['year'] > 1989)]
    coleliminar = ['date', 'city', 'country', 'neutral', 'day', 'month', 'year']
    df = df.drop(coleliminar, axis=1)
    df['tournament'] = df['tournament'].apply(tournament)
    df = df.loc[(df['tournament'] != 'No vale')]
    for index, row in df.iterrows():
        df.loc[index, 'home_points'] = points(row['home_score'], row['away_score'])
    for index, row in df.iterrows():
        df.loc[index, 'away_points'] = points(row['away_score'], row['home_score'])
    df = df[['home_team', 'away_team', 'home_points', 'away_points']]
    df[['home_team']] = df[['home_team']].apply(lambda x: x.str.upper())
    df[['away_team']] = df[['away_team']].apply(lambda x: x.str.upper())
    home = df.groupby('home_team', as_index=False).agg({'home_points': 'mean'})
    home = home.rename(columns = {'home_team': 'Country'})
    away = df.groupby('away_team', as_index=False).agg({'away_points':'mean'})
    away = away.rename(columns = {'away_team':'Country'})
    definitive = pd.merge(home, away, on='Country')
    definitive['MPP'] = definitive['home_points'] + definitive['away_points']
    definitive = definitive[['Country','MPP']]
    lista = ['ANDALUSIA', 'BASQUE COUNTRY', 'KERNOW', 'ARTSAKH', 'YORKSHIRE', 'YUGOSLAVIA', 'ABKHAZIA', 'JERSEY', 'CZECHOSLOVAKIA', 'MICRONESIA', 'GERMAN DR']
    definitive = definitive.loc[(~definitive['Country'].isin(lista))]
    definitive = definitive.sort_values(by='MPP', ascending = False)
    definitive = definitive.reset_index()
    definitive = definitive[['Country', 'MPP']]
    definitive['Position'] = definitive.index + 1
    definitive = definitive[['Position', 'Country', 'MPP']]
    p1 = list(definitive.loc[definitive['Country'] == c1, 'Position'])
    p1 = p1[0]
    p2 = list(definitive.loc[definitive['Country'] == c2, 'Position'])
    p2 = p2[0]
    return "{} have the {}th position and {} have the {}th position in football in the last 30 years based on their results.".format(c1, p1, c2, p2)