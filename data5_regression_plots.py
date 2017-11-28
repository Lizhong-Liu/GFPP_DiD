#!/usr/bin/env python

import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid", rc={'axes.linewidth': 2.5})
sns.set_context('notebook', font_scale=1.45, rc={"lines.linewidth": 3, "figure.figsize" : (7, 3)})

# From 2004 to 2015.
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

controls = ['FEMALE_RATIO', 'WHITE_RATIO', 'FRPM_RATE']
dependents = ['AC_TOTAL', 'AS_TOTAL', 'BC_TOTAL', 'F_TOTAL', 'TXS_TOTAL', 'UBS_TOTAL', 'HEALTH_TOTAL']

# Treatment group trend.
treatment = df[df['D'] == 1]
for y in dependents:
    formula2 = "{} ~ I + FEMALE_RATIO + WHITE_RATIO + FRPM_RATE".format(y)
    ols = smf.ols(formula=formula2, data=treatment)
    model = ols.fit()
    result = open("regression_results/df/Reg-treatment-{}.txt".format(y.lower()), "w")
    result.write(model.summary().as_text())

# Control group trend.
control = df[df['D'] == 0]
for y in dependents:
    formula3 = "{} ~ I + FEMALE_RATIO + WHITE_RATIO + FRPM_RATE".format(y)
    ols = smf.ols(formula=formula3, data=control)
    model = ols.fit()
    result = open("regression_results/df/Reg-control-{}.txt".format(y.lower()), "w")
    result.write(model.summary().as_text())

# Baseline balance test.
data = df[df['I'] == 0]
for c in controls:
    formula = "{} ~ D".format(c)
    ols = smf.ols(formula=formula, data=data)
    model = ols.fit()
    result = open("regression_results/df/Reg-baseline-{}.txt".format(y.lower()), "w")
    result.write(model.summary().as_text())

# DID analysis.
for y in dependents:
    formula3 = "{} ~ I + D + D*I + FEMALE_RATIO + WHITE_RATIO + FRPM_RATE".format(y)
    ols = smf.ols(formula=formula3, data=df)
    model = ols.fit()
    result = open("regression_results/df/Reg-did-{}.txt".format(y.lower()), "w")
    result.write(model.summary().as_text())

# Plot the trend for treatment and control group.
health_trend_t = df[df['D'] == 1].groupby('YEAR').mean()
for i in dependents:
    ax = health_trend_t['{}'.format(i)].plot()
    ax.set_xlabel('Year')
    ax.set_ylabel('{}'.format(i))
    plt.show()

health_trend_c = df[df['D'] == 0].groupby('YEAR').mean()
for i in dependents:
    health_trend_c['{}'.format(i)].plot()
    plt.show()

# Restrict samples to schools with data from 2011 to 2015.
# Robustness test.
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

# Baseline analysis.
baseline = df1[df1['I'] == 0]
for c in controls:
    ols = smf.ols(formula="{} ~ D".format(c), data=baseline)
    model = ols.fit()
    result = open("regression_results/df1/Reg-baseline-{}.txt".format(y.lower()), "w")
    result.write(model.summary().as_text())

# regplot.
for c in controls:
    plt.clf()
    ax = sns.regplot(x = "{}".format(c), y = "HEALTH_TOTAL", data = baseline[baseline['D'] == 1], scatter_kws = {"alpha" : 0.1})
    ax.set(title='{} - TREATMENT GROUP'.format(c))
    plt.savefig('plots/{}-treatment.pdf'.format(c))
for c in controls:
    plt.clf()
    ax = sns.regplot(x = "{}".format(c), y = "HEALTH_TOTAL", data = baseline[baseline['D'] == 0], scatter_kws = {"alpha" : 0.1})
    ax.set(title='{} - CONTROL GROUP'.format(c))
    plt.savefig('plots/{}-control.pdf'.format(c))

# DiD analysis.
for y in dependents:
    ols = smf.ols(formula="{} ~ I + D + D*I + FEMALE_RATIO + WHITE_RATIO + FRPM_RATE".format(y),
                  data=df1)
    model = ols.fit()
    result = open("regression_results/df1/Reg-didda-{}.txt".format(y.lower()), "w")
    result.write(model.summary().as_text())
