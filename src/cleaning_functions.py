def tournament(df):
    listtourn = ['CONCACAF Nations League', 'Gold Cup qualification', 'Oceania Nations Cup', 'Friendly', 'African Cup of Nations qualification', 'UEFA Euro', 'African Nations Championship qualifying', 'UEFA Nations League', 'African Cup of Nations', 'Copa América qualification', 'Gold Cup', 'FIFA World Cup', 'Oceania Nations Cup qualification', 'CONCACAF Nations League qualifying', 'Confederations Cup', 'UEFA Euro qualification', 'Copa América', 'FIFA World Cup qualification']
    return df.loc[df['tournament'].isin(listtourn)]

def points(row1,row2):
    row = 0
    if row1 > row2:
        row +=3
    elif row1 == row2:
        row +=1
    elif row1 < row2:
        row = 0
    return row