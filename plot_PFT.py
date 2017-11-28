#!/usr/bin/env python

import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df = pd.read_csv('school_merged.csv', sep='\t', low_memory=False)
df.rename(columns={'FRPM_%': 'FRPM_RATE'}, inplace=True)
df = df[df['FRPM_RATE'] != 'N / A']
df['FRPM_RATE'] = df['FRPM_RATE'].astype(float)
df.dropna(subset=['DISTRICT', 'SCHOOL', 'FRPM_RATE'], how='any', inplace=True)
df['D'] = 0
df.loc[df['DISTRICT'].str.contains('Unified'), 'D'] = 1
df['I'] = 0
df.loc[df['YEAR'] > 2012, 'I'] = 1
df.loc[df['YEAR'] < 2012, 'I'] = 0
df['D*I'] = df['I'] * df['D']

# narrow down to schools with data from 2011-2015
df1 = df[df['YEAR'] > 2010]
dic = {}
for i in df1['CDS_CODE']:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
keys = [i for i in dic if dic[i] == 5]
df1.set_index(['CDS_CODE', 'YEAR'], inplace=True)
df1 = df1.loc[keys, :]

# set controls and dependents list
controls = ['FEMALE_RATIO', 'WHITE_RATIO', 'FRPM_RATE']
dependents = ['AC_TOTAL', 'AS_TOTAL', 'BC_TOTAL', 'F_TOTAL', 'TXS_TOTAL', 'UBS_TOTAL', 'HEALTH_TOTAL']
df1.reset_index(inplace = True)

# Plot the trend for treatment and control group. (line)
for x in dependents:
    table = df1.pivot_table(values='{}'.format(x), index=['YEAR'], columns=['D'], aggfunc=np.mean)
    ax = table.plot()
    ax.get_legend().set_bbox_to_anchor((1.4, 1))
    ax.get_legend().set_title('Treatment Status')
    for t, l in zip(ax.get_legend().texts, ['Control','Treatment']): t.set_text(l)
    ax.set_xticks(range(2011,2016,1))
    ax.set(xlabel='Year',
       ylabel="Fraction",
       title='Fraction of students meeting healthy {} standards'.format(x.split('_')[0]))
    ax.figure.savefig("plots/line_{}.pdf".format(x), bbox_inches='tight', pad_inches=0.05)
    plt.show()
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
    ax.set(xlabel='Year',
           ylabel="Fraction",
           title='Fraction of students meeting healthy {} standards'.format(x.split('_')[0]))
    ax.figure.savefig("plots/violin_{}.pdf".format(x), bbox_inches='tight', pad_inches=0.05)
    plt.show()
    plt.clf()
