/* Create a sqlite database. */
CREATE TABLE school_enrollment (CDS_CODE INTEGER,
                                YEAR INTEGER, COUNTY TEXT, DISTRICT TEXT,
                                SCHOOL TEXT, ENR_TOTAL INTEGER, FEMALE_COUNT INTEGER,
                                FEMALE_RATIO REAL, WHITE_COUNT INTEGER, WHITE_RATIO REAL,
                                GR_1 INTEGER, GR_10 INTEGER, GR_11 INTEGER,
                                GR_12 INTEGER, GR_2 INTEGER, GR_3 INTEGER, GR_4 INTEGER,
                                GR_5 INTEGER, GR_6 INTEGER, GR_7 INTEGER, GR_8 INTEGER, GR_9 INTEGER,
                                KDGN INTEGER, UNGR_ELM INTEGER, UNGR_SEC INTEGER, ADULT INTEGER);
.mode csv
.import data/school_enrollment.csv school_enrollment
.mode columns


CREATE TABLE school_pft (CDS INTEGER, AC_5 REAL, AC_7 REAL,
                         AC_9 REAL, AC_total REAL, AS_5 REAL, AS_7 REAL, AS_9 REAL,
                         AS_total REAL, BC_5 REAL, BC_7 REAL, BC_9 REAL, BC_total REAL,
                         F_5 REAL, F_7 REAL, F_9 REAL,
                         F_total REAL, TXS_5 REAL, TXS_7 REAL, TXS_9 REAL, TXS_total REAL,
                         UBS_5 REAL, UBS_7 REAL,
                         UBS_9 REAL, UBS_total REAL, YEAR REAL, Health_5 REAL, Health_7 REAL,
                         Health_9 REAL, Health_total REAL);
.mode csv
.import data/school_pft.csv school_pft
.mode columns

CREATE TABLE school_frpm (IND INTEGER, YEAR INTEGER,
                          CCODE INTEGER, DCODE INTEGER, SCODE INTEGER, FRPM_RATE REAL,
                          FRPM_COUNT INTEGER, CDS_CODE INTEGER);
.mode csv
.import data/school_frpm.csv school_frpm
.mode columns
