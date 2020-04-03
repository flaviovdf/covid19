# -*- coding: utf8


from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
from rpy2.robjects.packages import importr

import rpy2.robjects as ro

epiestim = importr('EpiEstim')
_config = epiestim.make_config(min_mean_si=3.7,
                               mean_si=4.7,
                               max_mean_si=6,

                               min_std_si=1.9,
                               std_si=2.9,
                               std_mean_si=2.9,
                               max_std_si=4.9,

                               mean_prior=2.6,
                               std_prior=2,
                               si_parametric_distr='lognormal')


def make_config(**kwargs):
    return epiestim.make_config(**kwargs)


def estimate_r(df, config=None, method='parametric_si'):
    if config is None:
        global _config
        config = _config

    with localconverter(ro.default_converter + pandas2ri.converter):
        df = df.copy()
        if 'imported' in df.columns:
            if not (df['imported'] > 0).any():
                print('Ignoring imported column, all zeros')
                del df['imported']

        epiestim_result = epiestim.estimate_R(df,
                                              method=method,
                                              config=config)
        return pandas2ri.ri2py(epiestim_result[0])
