# -*- coding: utf8

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['lines.linewidth'] = 4

plt.style.use('seaborn-colorblind')
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

    mean = result_df['Mean(R)']
    x = np.arange(len(mean))
    plt.plot(x, mean, label='R0(t) +- .95CI')

    y_inf = result_df['Quantile.0.025(R)']
    y_sup = result_df['Quantile.0.975(R)']
    plt.fill_between(x, y_inf, y_sup, color='magenta', alpha=0.2)
    ax = plt.gca()
    if original_df is not None:
        xticks = original_df.index[(result_df['t_end'] - 1).astype('i').values]
        xticks = [flip_date(str(d)[5:10]) for d in xticks]
        plt.xticks(np.arange(len(xticks)))
        ax.set_xticklabels(xticks)
        plt.xticks(rotation=75)

    plt.ylim((0, y_sup.max() + 0.01))
    ax.axhline(1, linestyle='--', color='grey')
    plt.legend()
    plt.ylabel('R0(t)')
    plt.xlabel('Data - t')
    despine()
