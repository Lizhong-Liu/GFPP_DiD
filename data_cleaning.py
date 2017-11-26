#!/usr/bin/env python

import pandas as pd

# Dataframe of schools' CDS codes.
cds = pd.read_excel("data/pubschls.xls", usecols = ["CDSCode", "County", "District", "School"])
cds.rename(columns={"CDSCode": "CDS_CODE",
                   "County": "COUNTY",
                   "District": "DISTRICT",
                   "School": "SCHOOL"}, inplace=True)

# School enrollment data: 2001 - 2016.
file = ['0102', '0203', '0304', '0405', '0506', '0607']
for i in range(2007, 2016):
    file.append(str(i))

for_concat = []
for i in file:
    df = pd.read_table("data/{}.txt".format(i), index_col="CDS_CODE")
    df["YEAR"] = int(i)
    df["CDS_CODE"] = df.index
    for_concat.append(df)
results = pd.concat(for_concat, ignore_index=True)

YEAR = {}
first = 2001
for i in file[:6]:
    YEAR[i] = first + file.index(i)
for i, y in YEAR.items():
    results["YEAR"].replace(int(i), y, inplace=True)
enr_total = results.groupby(["CDS_CODE", "YEAR"]).sum()

    # Sex ratio amongst enrollment.
results["GENDER"].replace("F", 1, inplace=True)
results["GENDER"].replace("M", 0, inplace=True)
sex = results.loc[:, ["CDS_CODE", "YEAR", "GENDER", "ENR_TOTAL"]]
sex = sex.groupby(["CDS_CODE", "YEAR", "GENDER"]).sum()
sex = sex.iloc[sex.index.get_level_values("GENDER") == 1]
sex.reset_index(level=2, drop=True, inplace=True)
sex.rename(columns={"ENR_TOTAL": "FEMALE_COUNT"}, inplace=True)

la_enr = enr_total.join(sex, how="inner")
la_enr["FEMALE_RATIO"] = la_enr["FEMALE_COUNT"] / la_enr["ENR_TOTAL"]

    # Ethnic ratio amongst enrollment.
results.loc[results["ETHNIC"] != 7, "ETHNIC"] = 0
results.loc[results["ETHNIC"] == 7, "ETHNIC"] = 1
ethnic = results.loc[:, ["CDS_CODE", "YEAR", "ENR_TOTAL", "ETHNIC"]]
ethnic = ethnic.groupby(["CDS_CODE", "YEAR", "ETHNIC"]).sum()
ethnic = ethnic.iloc[ethnic.index.get_level_values("ETHNIC") == 1]
ethnic.reset_index(level=2, drop=True, inplace=True)
ethnic.rename(columns={"ENR_TOTAL": "WHITE_COUNT"}, inplace=True)

la_enr = la_enr.join(ethnic, how="inner")
la_enr["WHITE_RATIO"] = la_enr["WHITE_COUNT"] / la_enr["ENR_TOTAL"]
la_enr.drop("ETHNIC", axis=1, inplace=True)
la_enr = pd.merge(la_enr.reset_index(), cds,
                    on="CDS_CODE", how='left').set_index(['CDS_CODE','YEAR'])

    # Rearrange the columns.
cols = la_enr.columns.tolist()
cols = ['COUNTY','DISTRICT','SCHOOL','ENR_TOTAL','FEMALE_COUNT','FEMALE_RATIO','WHITE_COUNT','WHITE_RATIO','GR_1',
 'GR_10','GR_11','GR_12','GR_2','GR_3','GR_4','GR_5','GR_6','GR_7','GR_8','GR_9','KDGN','UNGR_ELM','UNGR_SEC','ADULT']
la_enr = la_enr[cols]

la_enr.to_csv("school_enrollment.csv", sep='\t', encoding='utf-8')
