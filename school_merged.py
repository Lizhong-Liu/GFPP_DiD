#!/usr/bin/env python

import pandas as pd

df = pd.read_csv("school_enrollment.csv", sep="\t", converters={"CDS_CODE": str}, index_col=[0,1])
df = df[df.index.get_level_values("CDS_CODE") // 10e11 == 19]

pft = pd.read_csv("PFT.csv", converters={"CDS_CODE": str})
pft.rename(columns={"CDS": "CDS_CODE", "AC_total": "AC_TOTAL", "AS_total": "AS_TOTAL", "BC_total": "BC_TOTAL",
                    "F_total": "F_TOTAL", "TXS_total": "TXS_TOTAL", "UBS_total": "UBS_TOTAL", "Health_total": "HEALTH_TOTAL"}, inplace=True)

pft = pft.loc[:, ["CDS_CODE", "YEAR", "AC_TOTAL", "AS_TOTAL", "BC_TOTAL", "F_TOTAL", "TXS_TOTAL", "UBS_TOTAL", "HEALTH_TOTAL"]]
pft.set_index(["CDS_CODE", "YEAR"], inplace=True)

la_gfpp = pd.merge(df.reset_index(), pft.reset_index(),
         on=["CDS_CODE", "YEAR"], how="inner").set_index(["CDS_CODE", "YEAR"])

la_gfpp.to_csv("gfpp_merged.csv", sep="\t", encoding="utf-8")
