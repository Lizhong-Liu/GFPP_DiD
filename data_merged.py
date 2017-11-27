#!/usr/bin/env python
import pandas as pd

df = pd.read_csv("school_enrollment.csv", sep="\t", converters={"CDS_CODE": str}, index_col=[0,1])
df = df[df.index.get_level_values("CDS_CODE") // 10e11 == 19]

pft = pd.read_csv("PFT.csv", converters={"CDS_CODE": str})
pft.rename(columns={"CDS": "CDS_CODE"}, inplace=True)
pft = pft.loc[:, ['CDS_CODE', 'YEAR', 'AC_5', 'AC_7', 'AC_9', 'AS_5', 'AS_7', 'AS_9','BC_5', 'BC_7',
                  'BC_9', 'F_5', 'F_7', 'F_9', 'TXS_5', 'TXS_7',
                  'TXS_9', 'UBS_5', 'UBS_7', 'Health_5', 'Health_7', 'Health_9']]
pft.set_index(["CDS_CODE", "YEAR"], inplace=True)

la_gfpp = pd.merge(df.reset_index(), pft.reset_index(),
         on=["CDS_CODE", "YEAR"], how="inner").set_index(["CDS_CODE", "YEAR"])

frpm = pd.read_csv("school_frpm.csv", sep="\t", usecols=[1,2,3,4], converters={"CDS_CODE": str})
frpm = frpm[frpm["CDS_CODE"].map(lambda x: x.startswith("19"))]
frpm["CDS_CODE"] = frpm["CDS_CODE"].astype(int)
frpm.set_index(["CDS_CODE", "YEAR"], inplace=True)
la_gfp = pd.merge(la_gfpp.reset_index(), frpm.reset_index(),
         on=["CDS_CODE", "YEAR"], how="inner").set_index(["CDS_CODE", "YEAR"])

la_gfp.to_csv("school_merged.csv", sep="\t", encoding="utf-8")
