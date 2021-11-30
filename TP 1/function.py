import pandas as pd

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