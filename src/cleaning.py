import pandas as pd
import cleaning_functions as cf

def database(c1, c2):
    df = pd.read_csv('../data-analysis-pipeline/Input/results.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df = df.loc[(df['year'] >= 1990)]
    coleliminar = ['date', 'city', 'country', 'neutral', 'day', 'month', 'year']
    df = df.drop(coleliminar, axis=1)
    df = cf.tournament(df)
    df = df.loc[(df['tournament'] != 'No vale')]
    for index, row in df.iterrows():
        df.loc[index, 'home_points'] = cf.points(row['home_score'], row['away_score'])
    for index, row in df.iterrows():
        df.loc[index, 'away_points'] = cf.points(row['away_score'], row['home_score'])
    df = df[['home_team', 'away_team', 'home_points', 'away_points']]
    df[['home_team', 'away_team']] = df[['home_team', 'away_team']].apply(lambda x: x.str.upper())
    home_df = df.groupby('home_team', as_index=False).agg({'home_points': 'mean'})
    home_df = home_df.rename(columns = {'home_team': 'Country'})
    away_df = df.groupby('away_team', as_index=False).agg({'away_points':'mean'})
    away_df = away_df.rename(columns = {'away_team':'Country'})
    definitive = pd.merge(home_df, away_df, on='Country')
    definitive['avg_points'] = definitive['home_points'] + definitive['away_points']
    definitive = definitive[['Country','avg_points']]
    lista = ['ANDALUSIA', 'BASQUE COUNTRY', 'KERNOW', 'ARTSAKH', 'YORKSHIRE', 'YUGOSLAVIA', 'ABKHAZIA', 'JERSEY', 'CZECHOSLOVAKIA', 'MICRONESIA', 'GERMAN DR']
    definitive = definitive.loc[(~definitive['Country'].isin(lista))]
    definitive = definitive.sort_values(by='avg_points', ascending = False)
    definitive = definitive.reset_index()
    definitive = definitive[['Country', 'avg_points']]
    definitive['Position'] = definitive.index + 1
    definitive = definitive[['Position', 'Country', 'avg_points']]
    p1 = list(definitive.loc[definitive['Country'] == c1, 'Position'])
    p1 = p1[0]
    p2 = list(definitive.loc[definitive['Country'] == c2, 'Position'])
    p2 = p2[0]
    return "{} have the {}th position and {} have the {}th position in football in the last 30 years based on their results.".format(c1, p1, c2, p2)