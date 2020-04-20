# -*- coding: utf8

from matplotlib.colors import ListedColormap
from scipy.interpolate import interp1d


import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['font.family'] = 'serif'
plt.rcParams['text.usetex'] = True

plt.style.use('tableau-colorblind10')
plt.rcParams['figure.figsize'] = (12, 8)


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
        print(date_txt)
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
    # x = np.arange(len(mean))

    x = original_df.index[(result_df['t_end'] - 1).astype('i').values]
    plt.plot(x, mean, c='k', zorder=1, alpha=.8)
    plt.annotate(r'R(t) = $%.2f \pm %.2f$ no dia %s' % (mean.values[-1],
                                                        pm.values[-1],
                                                        flip_date(str(x[-1]))),
                 (x[-1], mean.values[-1]),
                 xytext=(x[-7], mean.values[-1] + 1),
                 fontsize=14, horizontalalignment='center',
                 arrowprops=dict(arrowstyle='fancy',
                                 color='0.5',
                                 shrinkB=5))
    plt.scatter(x, mean, s=80, lw=.5, c=cmap(color_mapped(mean)),
                edgecolors='k', zorder=2)
    ax = plt.gca()
    ax.xaxis_date()

    # plt.plot(x, mean, label='R(t) +- .95CI')

    y_inf = result_df['Quantile.0.025(R)']
    y_sup = result_df['Quantile.0.975(R)']

    xi = np.arange(len(x))
    lowfn = interp1d(xi, y_inf, bounds_error=False, fill_value='extrapolate')
    highfn = interp1d(xi, y_sup, bounds_error=False, fill_value='extrapolate')
    plt.fill_between(x, lowfn(xi), highfn(xi), color='k', alpha=0.1, lw=0,
                     zorder=3)

    import pytz
    brt = pytz.timezone('America/Sao_Paulo')

    import matplotlib.dates as mdates
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(tz=brt))
    ax.xaxis.set_minor_locator(mdates.DayLocator(tz=brt))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m', tz=brt))
    plt.xticks(rotation=75)

    import datetime
    datenow = datetime.datetime.now()
    dstart = datetime.datetime(2020, 3, 1)
    plt.xlim(dstart, datenow)

    plt.ylim((0, y_sup.max() + 0.01))
    plt.yticks(np.arange(np.ceil(y_sup.max())))
    ax.axhline(1, linestyle='--', color='grey', zorder=4)
    # plt.legend()
    plt.ylabel(r'$R(t) \pm .95$ CI')
    plt.xlabel(r'Data - $t$')
    despine()
