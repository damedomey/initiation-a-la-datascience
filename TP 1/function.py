import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Retourne une liste triée des valeurs(distinctes) d'une colone d'un dataframe
def get_distinct(df, column):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Dataframe is required")
    else:
        df_column = df[column][df[column].notnull()]
        liste = df_column.sort_values().unique().tolist()
        for i in range(len(liste)):
            liste[i] = liste[i].lower()

        liste.sort()

        for i in range(len(liste)):
            if i == len(liste):
                break
            if liste[i-1] == liste[i]:
                del liste[i]
    return liste

# Statistiques d'un dataframe Pandas
def get_stats(df: pd.DataFrame, column: dict = [], save: bool = False ,filename: str = ''):
    columns = df.columns.values
    if column != []:
        columns = column
    x = np.arange(1, len(columns)+1)
    nan = []
    distinct = []
    values = []
    for column in columns:
        nan.append(df[column].isna().sum())
        distinct.append(df[column].nunique())
        values.append(df[column].notnull().sum())
    width = 0.2
    fig, ax = plt.subplots(figsize=(20,10), dpi=120)

    ax.set_xlim(xmin=0, xmax=len(columns)+1)
    ax.bar(x, nan, width, color='r')
    ax.bar(x+width, distinct, width, color='b')
    ax.bar(x+2*width, values, width, color='g')
    ax.bar(x+3*width, df.shape[0], width, color='y')
    ax.tick_params(axis='x', rotation=90)
    ax.set_xticks(x)
    ax.set_xticklabels(columns)
    ax.legend(('Valeurs nulles', 'Valeurs distinctes', 'Valeurs non nulles', 'Total'))

    new_df = pd.DataFrame({'Valeurs nulles': nan, 'Valeurs distinctes': distinct, 'Valeurs non nulles': values, 'Total': df.shape[0]})

    ax.table(cellText=new_df.T.values, colLabels=columns, rowLabels=new_df.columns, loc='top')
    if save:
        plt.savefig('data/images/{}'.format(filename))
