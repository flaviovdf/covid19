# -*- coding: utf8

import numpy as np
import pandas as pd


def load_data(fpath):
    df_tmp = pd.read_excel(fpath, sheet_name='Casos (FINAL)').fillna(0)
    columns = df_tmp['municipio']
    df_tmp = df_tmp[filter(lambda x: x.startswith('confirmados'),
                           df_tmp.columns[1:])]

    def to_date(txt):
        return pd.to_datetime('{}/2020 12:00:00'.format(txt[-5:].replace('_',
                                                                         '/')),
                              dayfirst=True)
    dates = pd.Index(map(to_date, df_tmp.columns))
    new_index = pd.date_range(start=dates[-1] - np.timedelta64(1, 'D'),
                              end=dates[0], freq='1D')

    rv = pd.DataFrame(columns=columns.values, index=new_index)
    aux = pd.DataFrame(df_tmp.values.T,
                       index=dates,
                       columns=columns.values)
    importados = aux['Importados/Indefinidos'].copy().fillna(0)
    del aux['Importados/Indefinidos']
    del rv['Importados/Indefinidos']

    aux[aux == 0] = np.nan
    rv.loc[aux.index] = aux
    rv.loc[rv.index[0]] = 0
    rv = rv.sort_index().fillna(method='ffill')
    rv['Importados/Indefinidos'] = importados

    rv = rv.fillna(0)
    rv = rv.diff().iloc[1:]
    rv[rv < 0] = 0

    return rv


def get_state(full_df, state):
    work_df = full_df[['state', 'city', 'place_type',
                       'confirmed', 'deaths']].copy()
    work_df.index = pd.to_datetime(full_df['date'])
    work_df = work_df.sort_index()

    idx = (work_df['state'] == state) & (work_df['place_type'] == 'state')
    state_df = work_df[idx]

    first_day = np.nonzero(state_df.values)[0][0]
    state_df = state_df[first_day:]

    first = state_df['confirmed'].iloc[0]
    state_df['confirmed'] = state_df['confirmed'].diff().fillna(0).copy()
    state_df['confirmed'].values[state_df['confirmed'] < 0] = 0
    state_df['confirmed'].values[0] = first

    first = state_df['deaths'].iloc[0]
    state_df['deaths'] = state_df['deaths'].diff().fillna(0).copy()
    state_df['deaths'].values[state_df['deaths'] < 0] = 0
    state_df['deaths'].values[0] = first

    idx = (work_df['state'] == state) & \
        (work_df['city'] == 'Importados/Indefinidos')
    imported_df = work_df[idx]['confirmed']

    state_df['imported'] = imported_df
    state_df = state_df.rename(columns={'confirmed': 'local'}).fillna(0).copy()
    last_day = np.nonzero(state_df['local'].values)[0][-1]

    return state_df.iloc[:last_day+1].copy()


def get_city(full_df, state, city):
    work_df = full_df[['state', 'city', 'place_type',
                       'confirmed', 'deaths']].copy()

    work_df.index = pd.to_datetime(full_df['date'])
    work_df = work_df.sort_index()

    idx = (work_df['state'] == state) & (work_df['city'] == city)

    city_df = work_df[idx]
    first_day = np.nonzero(city_df.values)[0][0]
    city_df = city_df[first_day:]

    first = city_df['confirmed'].iloc[0]
    city_df['confirmed'] = city_df['confirmed'].diff().fillna(0).copy()
    city_df['confirmed'].values[city_df['confirmed'] < 0] = 0
    city_df['confirmed'].values[0] = first

    first = city_df['deaths'].iloc[0]
    city_df['deaths'] = city_df['deaths'].diff().fillna(0).copy()
    city_df['deaths'].values[city_df['deaths'] < 0] = 0
    city_df['deaths'].values[0] = first

    city_df = city_df.rename(columns={'confirmed': 'local'}).fillna(0).copy()
    last_day = np.nonzero(city_df['local'].values)[0][-1]

    return city_df.iloc[:last_day+1].copy()
