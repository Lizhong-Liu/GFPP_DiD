#!/usr/bin/env python

import pandas as pd
dflist = []
for yr in range(2001,2011):
    df = pd.read_table('PFT_{}/PhysFit{}.txt'.format(yr,yr), delimiter = ',', low_memory = False)
    df.rename(columns = {'Scode': 'SCHL',
                         'Ccode': 'CO',
                         'Dcode': 'DIST'}, inplace = True)
    df = df[(df['SCHL']!=0) & (df['CO']==19) & (df['DIST']!=0) & (df['RptType']==1)&(df['SubGrp']==0)&(df['Level']==1)]
    df['CDS'] = df['CO'].astype(str)+df['DIST'].astype(str)+df['SCHL'].astype(str)
    for x in (5,7,9):
        df.loc[df['Gr'+str(x)+'PctIn'] == '*','Gr0'+str(x)+'_Stu'] = 0
        df['Gr'+str(x)+'PctIn'].replace("*", 0, inplace=True)
        df['NoHFZ'+str(x)] = df['Gr'+str(x)+'PctIn'].astype(float)*df['Gr0'+str(x)+'_Stu'].astype(int)/100
        df['NoHFZ'+str(x)] = df['NoHFZ'+str(x)].round().astype(int)
        df['Gr0'+str(x)+'_Stu'] = df['Gr0'+str(x)+'_Stu'].astype(int)
        df.rename(columns={'line_num':'Line_Text'}, inplace = True)
    df = df.groupby(by = ['CDS','Line_Text'])['Gr05_Stu','NoHFZ5','Gr07_Stu','NoHFZ7','Gr09_Stu','NoHFZ9'].sum()
    for x in (5,7,9):
        df['Perh'+str(x)] = df['NoHFZ'+str(x)]/df['Gr0'+str(x)+'_Stu']
    df['Perh'] = (df.NoHFZ5+df.NoHFZ7+df.NoHFZ9)/(df.Gr05_Stu+df.Gr07_Stu+df.Gr09_Stu)

    # unstack fitness areas columns
    df = df.reset_index()
    grd_5 = df.pivot_table(index='CDS', columns='Line_Text', values='Perh5').dropna()
    grd_7 = df.pivot_table(index='CDS', columns='Line_Text', values='Perh7').dropna()
    grd_9 = df.pivot_table(index='CDS', columns='Line_Text', values='Perh9').dropna()
    total = df.pivot_table(index='CDS', columns='Line_Text', values='Perh').dropna()

    # merge tables
    grd_5.rename(columns={1: 'AC_5',
                  2: 'BC_5',
                  3: 'AS_5',
                  4: 'TXS_5',
                  5: 'UBS_5',
                  6: 'F_5'
                       }, inplace=True)
    grd_7.rename(columns={1: 'AC_7',
                  2: 'BC_7',
                  3: 'AS_7',
                  4: 'TXS_7',
                  5: 'UBS_7',
                  6: 'F_7'
                       }, inplace=True)
    grd_9.rename(columns={1: 'AC_9',
                  2: 'BC_9',
                  3: 'AS_9',
                  4: 'TXS_9',
                  5: 'UBS_9',
                  6: 'F_9'
                       }, inplace=True)
    total.rename(columns={1: 'AC_total',
                  2: 'BC_total',
                  3: 'AS_total',
                  4: 'TXS_total',
                  5: 'UBS_total',
                  6: 'F_total'
                       }, inplace=True)
    result = grd_5.join(grd_7, how='outer')
    result = result.join(grd_9, how='outer')
    result = result.join(total, how='outer')
    result['YEAR'] = int(yr)
    dflist.append(result)

for yr in range(2011,2017):
    if yr < 2012:
        df = pd.read_table('PFT_{}/PhysFit{}.txt'.format(yr,yr), delimiter = ',', low_memory = False)
    elif yr > 2013:
        df = pd.read_table('PFT_{}/{}_ResearchFile.txt'.format(yr,str(yr-1)+'_'+str(yr)[2:]), delimiter = ',', low_memory = False)
    else:
        df = pd.read_table('PFT_{}/{}_ResearchFile.txt'.format(yr,str(yr-1)+'_'+str(yr)[2:]), delimiter = '\t', low_memory = False)

    # group test results by school code and fitness areas
    df = df[(df['SCHL']!=0) & (df['CO']==19) & (df['DIST']!=0) & (df['Report_Number']==0)&(df['Table_Number']==1)&(df['Level_Number']==1)]
    df['CDS'] = df['CO'].astype(str)+df['DIST'].astype(str)+df['SCHL'].astype(str)
    df['Line_Text'] = df['Line_Text'].str.rstrip()
    for x in (5,7,9):
        df.loc[df['NoHFZ'+str(x)] == '**','NoStud'+str(x)] = 0
        df['NoHFZ'+str(x)].replace("**", 0, inplace=True)
        df['NoHFZ'+str(x)] = df['NoHFZ'+str(x)].astype(int)
    df = df.groupby(by = ['CDS','Line_Text'])['NoStud5','NoHFZ5','NoStud7','NoHFZ7','NoStud9','NoHFZ9'].sum()
    for x in (5,7,9):
        df['Perh'+str(x)] = df['NoHFZ'+str(x)]/df['NoStud'+str(x)]
    df['Perh'] = (df.NoHFZ5+df.NoHFZ7+df.NoHFZ9)/(df.NoStud5+df.NoStud7+df.NoStud9)

    # unstack fitness areas columns
    df = df.reset_index()
    grd_5 = df.pivot_table(index='CDS', columns='Line_Text', values='Perh5').dropna()
    grd_7 = df.pivot_table(index='CDS', columns='Line_Text', values='Perh7').dropna()
    grd_9 = df.pivot_table(index='CDS', columns='Line_Text', values='Perh9').dropna()
    total = df.pivot_table(index='CDS', columns='Line_Text', values='Perh').dropna()

    # merge tables
    grd_5.rename(columns={'Abdominal Strength': 'AS_5',
                  'Aerobic Capacity': 'AC_5',
                  'Body Composition': 'BC_5',
                  'Flexibility': 'F_5',
                  'Trunk Extension Strength': 'TXS_5',
                        'Upper Body Strength': 'UBS_5'
                       }, inplace=True)
    grd_7.rename(columns={'Abdominal Strength': 'AS_7',
                  'Aerobic Capacity': 'AC_7',
                  'Body Composition': 'BC_7',
                  'Flexibility': 'F_7',
                  'Trunk Extension Strength': 'TXS_7',
                    'Upper Body Strength': 'UBS_7'
                       }, inplace=True)
    grd_9.rename(columns={'Abdominal Strength': 'AS_9',
                  'Aerobic Capacity': 'AC_9',
                  'Body Composition': 'BC_9',
                  'Flexibility': 'F_9',
                  'Trunk Extension Strength': 'TXS_9',
                    'Upper Body Strength': 'UBS_9'
                       }, inplace=True)
    total.rename(columns={'Abdominal Strength': 'AS_total',
                  'Aerobic Capacity': 'AC_total',
                  'Body Composition': 'BC_total',
                  'Flexibility': 'F_total',
                  'Trunk Extension Strength': 'TXS_total',
                        'Upper Body Strength': 'UBS_total'
                       }, inplace=True)
    result = grd_5.join(grd_7, how='outer')
    result = result.join(grd_9, how='outer')
    result = result.join(total, how='outer')
    result['YEAR'] = int(yr)
    dflist.append(result)
df = pd.concat(dflist)
df['Health_5'] =  (df.AS_5 + df.AC_5 + df.BC_5 + df.F_5 + df.TXS_5 + df.UBS_5)/6
df['Health_7'] =  (df.AS_7 + df.AC_7 + df.BC_7 + df.F_7 + df.TXS_7 + df.UBS_7)/6
df['Health_9'] =  (df.AS_9 + df.AC_9 + df.BC_9 + df.F_9 + df.TXS_9 + df.UBS_9)/6
df['Health_total'] =  (df.AS_total + df.AC_total + df.BC_total + df.F_total + df.TXS_total + df.UBS_total)/6
df.to_csv('PFT.csv')
