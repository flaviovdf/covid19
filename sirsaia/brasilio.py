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
