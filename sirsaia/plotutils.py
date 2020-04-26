# -*- coding: utf8

from matplotlib.colors import ListedColormap
from scipy.interpolate import interp1d


import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pytz


def init_matplotlib():
    plt.rcParams['axes.labelsize'] = 24
    plt.rcParams['axes.titlesize'] = 24
    plt.rcParams['legend.fontsize'] = 24
    plt.rcParams['xtick.labelsize'] = 24
    plt.rcParams['ytick.labelsize'] = 24
    plt.rcParams['lines.linewidth'] = 3
    plt.rcParams['font.family'] = 'serif'
    # plt.rcParams['text.usetex'] = True


def despine(ax=None):
    if ax is None:
        ax = plt.gca()

    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')


def plot_result(result_df, original_df=None):
    def flip_date(date_txt):
        y, m = date_txt[:10].split('-')[1:3]
        return '/'.join([m, y])

    def color_mapped(y):
        return np.clip(y, .5, 1.5) - .5

    ABOVE = [1, 0, 0]
    MIDDLE = [1, 1, 1]
    BELOW = [0, 0, 0]
    cmap = ListedColormap(np.r_[
        np.linspace(BELOW, MIDDLE, 25),
        np.linspace(MIDDLE, ABOVE, 25)])

    mean = result_df['Mean(R)']
    pm = (result_df['Quantile.0.975(R)'] - result_df['Quantile.0.025(R)']) / 2

    x = original_df.index[(result_df['t_end'] - 1).astype('i').values]
    plt.plot(x, mean, c='k', zorder=1, alpha=.8)
    plt.annotate(r'R(t) = $%.2f \pm %.2f$ no dia %s' % (mean.values[-1],
                                                        pm.values[-1],
                                                        flip_date(str(x[-1]))),
                 (x[-1], mean.values[-1]),
                 xytext=(x[-7], mean.values[-1] + 2),
                 fontsize=24, horizontalalignment='center',
                 arrowprops=dict(arrowstyle='fancy',
                                 color='0.5',
                                 shrinkB=5))
    plt.scatter(x, mean, s=160, lw=1, c=cmap(color_mapped(mean)),
                edgecolors='k', zorder=2)
    ax = plt.gca()
    ax.xaxis_date()

    y_inf = result_df['Quantile.0.025(R)']
    y_sup = result_df['Quantile.0.975(R)']

    xi = np.arange(len(x))
    lowfn = interp1d(xi, y_inf, bounds_error=False, fill_value='extrapolate')
    highfn = interp1d(xi, y_sup, bounds_error=False, fill_value='extrapolate')
    plt.fill_between(x, lowfn(xi), highfn(xi), color='k', alpha=0.1, lw=0,
                     zorder=3)

    brt = pytz.timezone('America/Sao_Paulo')

    ax.xaxis.set_major_locator(mdates.WeekdayLocator(tz=brt))
    ax.xaxis.set_minor_locator(mdates.DayLocator(tz=brt))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m', tz=brt))
    plt.xticks(rotation=75)

    plt.ylim((0, y_sup.max() + 0.01))
    plt.yticks(np.arange(np.ceil(y_sup.max())))
    ax.axhline(1, linestyle='--', color='grey', zorder=4)

    plt.title('Infectividade Estimada')
    plt.ylabel(r'$R(t) \pm .95$ CI')
    plt.xlabel(r'Data - $t$')
    despine()


def plot_it(df, deaths=False):
    if deaths:
        data = df.deaths
    else:
        data = df.local

    plt.plot(df.index, data, c='k', zorder=1, alpha=.8)
    plt.scatter(df.index, data, s=160, lw=1, edgecolors='k', zorder=2)

    brt = pytz.timezone('America/Sao_Paulo')

    ax = plt.gca()
    ax.xaxis_date(tz=brt)
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(tz=brt))
    ax.xaxis.set_minor_locator(mdates.DayLocator(tz=brt))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m', tz=brt))

    plt.xticks(rotation=75)
    if deaths:
        plt.title('Mortes Confirmadas M(t) por dia')
        plt.ylabel('M(t)')
    else:
        plt.title('Casos Confirmados I(t) por dia')
        plt.ylabel('I(t)')

    plt.xlabel('Data - t')
    # plt.ylim((0, data.values.max() + 10))


def plot_weekdiff(df):

    df = df[['local']].resample('W-Sat').sum().copy()
    first = df.iloc[0]

    df = df.diff().copy()
    df.iloc[0] = first
    df = df.iloc[:-1]

    positive = df > 0
    plt.plot(df.index, df.local, c='k', zorder=1, alpha=.8)

    if (~positive).sum().any():
        plt.scatter(df[~positive].index, df[~positive].local, s=160, lw=1,
                    edgecolors='k', zorder=2, color='g')

    plt.scatter(df[positive].index, df[positive].local, color='r',
                s=160, lw=1, edgecolor='k', zorder=2)

    brt = pytz.timezone('America/Sao_Paulo')

    ax = plt.gca()
    ax.xaxis_date(tz=brt)
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(tz=brt,
                                                     byweekday=mdates.SA))
    ax.xaxis.set_minor_locator(mdates.DayLocator(tz=brt))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m', tz=brt))
    ax.axhline(0, linestyle='--', color='grey', zorder=4)

    # plt.ylim((0, df.values.max() + 10))
    plt.xticks(rotation=75)
    plt.title('Diferença Entre Soma de Casos da Semana')
    plt.ylabel('I(w) - I(w-1)')
    plt.xlabel('Semana - w')
