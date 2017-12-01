SELECT *,
     I * D AS [D*I]
FROM (
SELECT school_pft.CDS AS CDS_CODE,
       school_pft.YEAR AS YEAR,
       school_pft.AC_TOTAL AS AC_TOTAL,
       school_pft.AS_TOTAL AS AS_TOTAL,
       school_pft.BC_TOTAL AS BC_TOTAL,
       school_pft.F_TOTAL AS F_TOTAL,
       school_pft.TXS_TOTAL AS TXS_TOTAL,
       school_pft.UBS_TOTAL AS UBS_TOTAL,
       school_pft.HEALTH_TOTAL AS HEALTH_TOTAL,
       school_frpm.FRPM_COUNT AS FRPM_COUNT,
       school_frpm.FRPM_RATE AS FRPM_RATE,
       school_enrollment.ENR_TOTAL AS ENR_TOTAL,
       school_enrollment.FEMALE_COUNT AS FEMALE_COUNT,
       school_enrollment.FEMALE_RATIO AS FEMALE_RATIO,
       school_enrollment.WHITE_COUNT AS WHITE_COUNT,
       school_enrollment.WHITE_RATIO AS WHITE_RATIO,
       school_enrollment.DISTRICT LIKE '%Unified%' AS D,
       school_pft.YEAR > 2011 AS I
FROM school_enrollment
INNER JOIN school_frpm ON
     school_frpm.CDS_CODE = school_enrollment.CDS_CODE AND
     school_frpm.YEAR = school_enrollment.Year
INNER JOIN school_pft ON
     school_pft.CDS = school_enrollment.CDS_CODE AND
     school_pft.YEAR = school_enrollment.Year
WHERE FRPM_RATE != 'N / A' AND
      FRPM_RATE != '' AND
      FRPM_COUNT != 'N / A' AND
      FRPM_COUNT != '' AND
      DISTRICT > 0 AND
      SCHOOL > 0 );
