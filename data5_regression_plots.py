#!/usr/bin/env python

import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
sns.set_style("whitegrid", rc={'axes.linewidth': 2.5})
sns.set_context('notebook', font_scale=1.45, rc={"lines.linewidth": 3, "figure.figsize" : (7, 3)})

con = sqlite3.connect("school_gfpp.sqlite")
with open("data4_merge.sql") as f: df = pd.read_sql(f.read(), con)

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

# Baseline analysis and balance test.
data = df[df['I'] == 0]
tab = data.groupby(by='D').mean()[['ENR_TOTAL','FEMALE_COUNT','FEMALE_RATIO','WHITE_COUNT','WHITE_RATIO','FRPM_COUNT','FRPM_RATE']]
tab.index.name = None
tab = tab.transpose().rename(columns={0:'Treatment',1:'Control'})
tab = tab.round(decimals=2)
print(tab)

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
health_trend_t = treatment.groupby('YEAR', as_index=False).mean()
health_trend_t['YEAR'].astype(int, inplace=True)
ax = health_trend_t.plot(x='YEAR', y=['AC_TOTAL', 'AS_TOTAL', 'BC_TOTAL', 'F_TOTAL','TXS_TOTAL', 'UBS_TOTAL', 'HEALTH_TOTAL'])
plt.ylabel('Fraction of Students Passed')
plt.xlabel('Year')
plt.title('Fraction of Students Passed the Physical Fitness Tests')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
ax.figure.savefig('line_health_trend_treatment.pdf')

health_trend_c = control.groupby('YEAR', as_index=False).mean()
health_trend_c['YEAR'].astype(int, inplace=True)
ax = health_trend_c.plot(x='YEAR', y=['AC_TOTAL', 'AS_TOTAL', 'BC_TOTAL', 'F_TOTAL','TXS_TOTAL', 'UBS_TOTAL', 'HEALTH_TOTAL'])
plt.ylabel('Fraction of Students Passed')
plt.xlabel('Year')
plt.title('Fraction of Students Passed the Physical Fitness Tests')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
ax.figure.savefig('line_health_trend_control.pdf')

# Restrict samples to schools with data from 2011 to 2015.
# Robustness test r1.
df1 = df[df['YEAR'] > 2010]
dic = {}
for i in df1['CDS_CODE']:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
keys = [i for i in dic if dic[i] == 5]
df1.set_index('CDS_CODE', inplace=True)
df1 = df1.loc[keys, :]

# Baseline analysis.
baseline = df1[df1['I'] == 0]
tab = baseline.groupby(by='D').mean()[['ENR_TOTAL','FEMALE_COUNT','FEMALE_RATIO','WHITE_COUNT','WHITE_RATIO','FRPM_COUNT','FRPM_RATE']]
tab.index.name = None
tab = tab.transpose().rename(columns={0:'Treatment',1:'Control'})
tab = tab.round(decimals=2)
print(tab)

for c in controls:
    ols = smf.ols(formula="{} ~ D".format(c), data=baseline)
    model = ols.fit()
    result = open("regression_results/df1/Reg-baseline-{}.txt".format(y.lower()), "w")
    result.write(model.summary().as_text())

# Resample health trend.
treatment1 = df1[df1['D'] == 1]
health_trend_t1 = treatment1.groupby('YEAR', as_index=False).mean()
health_trend_t1['YEAR'].astype(int, inplace=True)
ax = health_trend_t1.plot(x='YEAR', y=['AC_TOTAL', 'AS_TOTAL', 'BC_TOTAL', 'F_TOTAL','TXS_TOTAL', 'UBS_TOTAL', 'HEALTH_TOTAL'])
plt.ylabel('Fraction of Students Passed')
plt.xlabel('Year')
plt.title('Fraction of Students Passed the Physical Fitness Tests')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
ax.figure.savefig('line_health_trend_treatment_resample.pdf')

control1 = df1[df1['D'] == 0]
health_trend_c1 = control1.groupby('YEAR', as_index=False).mean()
health_trend_c1['YEAR'].astype(int, inplace=True)
ax = health_trend_c1.plot(x='YEAR', y=['AC_TOTAL', 'AS_TOTAL', 'BC_TOTAL', 'F_TOTAL','TXS_TOTAL', 'UBS_TOTAL', 'HEALTH_TOTAL'])
plt.ylabel('Fraction of Students Passed')
plt.xlabel('Year')
plt.title('Fraction of Students Passed the Physical Fitness Tests')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
ax.figure.savefig('line_health_trend_control_resample.pdf')

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

# Robustness test 2: fixed effect model.
fe = df1.reset_index()
fe_mean = fe.groupby('CDS_CODE', as_index=False).mean()
d_means = [fe_mean.loc[0, i] for i in dependents]
for i in range(len(d_means)):
    fe.loc[:, dependents[i]] = fe['{}'.format(dependents[i])] - d_means[i]
c_means = [fe_mean.loc[0, i] for i in controls]
for i in range(len(c_means)):
    fe.loc[:, controls[i]] = fe['{}'.format(controls[i])] - c_means[i]

for y in dependents:
    ols = smf.ols(formula="{} ~ D + ENR_TOTAL + FEMALE_RATIO + WHITE_RATIO + FRPM_RATE".format(y), data=fe)
    model = ols.fit()
    result = open("regression_results/df1/Reg-fe-{}.txt".format(y.lower()), "w")
    result.write(model.summary().as_text())
