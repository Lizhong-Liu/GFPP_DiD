#!/usr/bin/env python

import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

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
    print(model.summary())

# Control group trend.
control = df[df['D'] == 0]
for y in dependents:
    formula3 = "{} ~ I + FEMALE_RATIO + WHITE_RATIO + FRPM_RATE".format(y)
    ols = smf.ols(formula=formula3, data=control)
    model = ols.fit()
    print(model.summary())

# Baseline balance test.
data = df[df['I'] == 0]
for c in controls:
    formula = "{} ~ D".format(c)
    ols = smf.ols(formula=formula, data=data)
    model = ols.fit()
    print(model.summary())

# DID analysis.
for y in dependents:
    formula3 = "{} ~ I + D + D*I + FEMALE_RATIO + WHITE_RATIO + FRPM_RATE".format(y)
    ols = smf.ols(formula=formula3, data=df)
    model = ols.fit()
    print(model.summary())

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
