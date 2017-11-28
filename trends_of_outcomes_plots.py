#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from data_regression import df1, dependents

df1.reset_index(inplace=True)
# Plot the trend for treatment and control group. (line)
for x in dependents:
    table = df1.pivot_table(values='{}'.format(x), index=['YEAR'], columns=['D'], aggfunc=np.mean)
    ax = table.plot()
    ax.get_legend().set_bbox_to_anchor((1.4, 1))
    ax.get_legend().set_title('Treatment Status')
    for t, l in zip(ax.get_legend().texts, ['Control','Treatment']): t.set_text(l)
    ax.set_xticks(range(2011,2016,1))
    ax.set(xlabel = 'Year',
       ylabel = "Fraction",
       title = 'Fraction of students meeting healthy {} standards'.format(x.split('_')[0]))
    ax.figure.savefig("plots/line_{}.pdf".format(x), bbox_inches='tight', pad_inches=0.05)
    plt.clf()

# Plot the spread shape for treatment and control group. (violin)
sns.set_style("whitegrid", rc={'axes.linewidth': 2.5})
sns.set_context('notebook', font_scale=1.45, rc={"lines.linewidth": 3, "figure.figsize" : (7, 3)})
for x in dependents:
    ax = sns.violinplot(x = "YEAR", y = "{}".format(x), data = df1,
                        hue = "D", split = True, bw = 0.1, cut = 0,
                        linewidth = 2)
    ax.get_legend().set_bbox_to_anchor((1.4, 1))
    ax.get_legend().set_title('Treatment Status')
    for t, l in zip(ax.get_legend().texts, ['Control','Treatment']): t.set_text(l)
    ax.set_ylim(0, 1)
    ax.set(xlabel = 'Year',
           ylabel = "Fraction",
           title = 'Fraction of students meeting healthy {} standards'.format(x.split('_')[0]))
    ax.figure.savefig("plots/violin_{}.pdf".format(x), bbox_inches='tight', pad_inches=0.05)
    plt.clf()
