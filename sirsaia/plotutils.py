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
        y, m = date_txt.split('-')
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
    x = np.arange(len(mean))

    plt.plot(x, mean, c='k', zorder=1, alpha=.8)
    plt.scatter(x, mean, s=80, lw=.5, c=cmap(color_mapped(mean)),
                edgecolors='k', zorder=2)

    # plt.plot(x, mean, label='R(t) +- .95CI')

    y_inf = result_df['Quantile.0.025(R)']
    y_sup = result_df['Quantile.0.975(R)']

    lowfn = interp1d(x, y_inf, bounds_error=False, fill_value='extrapolate')
    highfn = interp1d(x, y_sup, bounds_error=False, fill_value='extrapolate')
    plt.fill_between(x, lowfn(x), highfn(x), color='k', alpha=0.1, lw=0,
                     zorder=3)

    ax = plt.gca()
    if original_df is not None:
        xticks = original_df.index[(result_df['t_end'] - 1).astype('i').values]
        xticks = [flip_date(str(d)[5:10]) for d in xticks]
        plt.xticks(np.arange(len(xticks))[::2])
        ax.set_xticklabels(xticks[::2])
        plt.xticks(rotation=75)

    plt.ylim((0, y_sup.max() + 0.01))
    plt.yticks(np.arange(np.ceil(y_sup.max())))
    ax.axhline(1, linestyle='--', color='grey')
    # plt.legend()
    plt.ylabel(r'$R(t) \pm .95$ CI')
    plt.xlabel(r'Data - $t$')
    despine()
