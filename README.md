# Good Food Purchasing Program in LA: Socio-economic Impacts and Implications
## PPHA 30550/1 - Final Project
**Group Member: [Manyi Wang](@manyiw), [Yiran Hao](@chiertu), [Lizhong Liu](@Lizhong-Liu)**


#### GFPP Overview
Good Food Purchasing Program (GFPP) is an initiative currently implemented in several municipalities such as Los Angeles, San Francisco, and New York, which is mainly adopted by public institutions (public schools, municipalities, etc.). The bodies practicing such program restrict their purchase of meals by standards of nutrition, of raw material sources, and of envrionmental influences. GFPP has five value criteria: animal welfare, nutrition, support for local business, rights of employees (such as safety and justice), and environmental sustainability. 

A more insightful overview of GFPP can be found on the website of [Center for Good Food Purchasing](https://goodfoodpurchasing.org/program-overview/). You can also find details of LA's GFPP practice [here](http://goodfoodla.org/good-food/) and [here](https://achieve.lausd.net/Page/11672).


#### Project Goal
Our project aims to identify the causal relations between the implementation of this program and local socio-economic development by applying a Difference-in-difference (DiD) analysis. As GFPP has been marked as a priority in several other cities, including Austin, Chicago, Cincinnati, New York, Oakland and Twin Cities, and there lack quantitative evaluation of the program, our project can serve as a reference for these other cities in the potential outcomes of GFPP.


#### Project Design
Since Los Angeles is the very first city piloting the program, we mark LA as our "city of interest". Given the fact that GFPP is mainly adopted by LA Unified School District (LAUSD), other schools outside of LAUSD (but still in LA county) are therefore ideal as a control group in our analysis. We utilize school-level data from [California Department of Education](https://www.cde.ca.gov/) and focus on the change of students' physical performance (measured by [physical fitness test](https://www.cde.ca.gov/ta/tg/pf/) records) before and after the implementation of GFPP between schools in LAUSD and other schools outside of LAUSD.


#### Variables and Data Source
Our model tries to test the potential impacts of GFPP based on mutiple socio-economic indicators: health, human capital (education), and household economic development. Within these three categories, we further specify the variables in our regression analysis as following:
Dependent variable:
- Health (pft):
  - [Physical Fitness (California Department of Education (CDE))](https://www.cde.ca.gov/ta/tg/pf/pftresearch.asp)
Independent variables:
- School Demographics:
  - [Enrollment (CDE)](https://www.cde.ca.gov/ds/sd/sd/filesenr.asp);
  - [Demographics (CDE)](https://www.cde.ca.gov/ds/sd/sd/filesenr.asp);
- Household Economic Development (frpm):
  - [School-level Poverty Rate (CDE)](https://www.cde.ca.gov/ds/sd/sd/filessp.asp);

Besides regressional analysis, we also want to examine the potential influence of GFPP on LA's local food business. Unfortunately, for now there is little available micro-level data on it, so we cannot include it in our regression model. Instead, we use American Community Survey data on county level and plot an interactive map to show the growth of different food-related sectors (including Agriculture, Food Services, Retail, and Wholesale). The source of data can be found via this [link](https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml?refresh=t).



#### Project Guideline
We divide the project into two parts: regression analysis and ACS analysis. For the first part - regression analysis, all codes can be found in this repository (named as "data_something.py" or "plot_something.py"). We do the following to get the regression results:
- Data cleaning: 
  - Data from CDE are recorded annually in .csv files or .xls files. Thus, we clean each variable up by year and concat them on CDS code (the identification code for each school). You can find three files recording the codes of data cleaning:
    - School enrollment and demographics: data1_enrollment.py
    - School-level physical fitness test results: data2_pft.py
    - School-level poverty data (we use school-level enrollment rate of the [Free and Reduced Price Meals Program](https://www.fns.usda.gov/school-meals/applying-free-and-reduced-price-school-meals) as a proxy: data3_frpm.py
  - With the codes above, we create three .csv files storing these three variables. We also use these .csv files to create a sqlite database which is available to the public for future reference. All these data files are saved in the folder - "data":
    - School enrollment and demographics: school_enrollment.csv
    - School-level physical fitness test results: school_pft.csv
    - School-level poverty: school_pft.csv
    - Create a sqlite database: data4_create_db.sql
    - Sqlite database: school_gfpp.sqlite (This file is saved in the root directory of this repo)
- Data merging:
  - We then use sqlite language to merge the tables in school_gfpp.sqlite. You can find the code recorded in:
    - Sqlite merge tables: data4_merge.sql
  - We also use pandas to merge data and generate a merged .csv file (also saved in "data" folder):
    - Merged .csv table: school_merged.csv (just for future reference)
- Regression analysis:
  - We first apply the DiD model on the entire dataset, but find that in 2011, the physical fitness test records fluctuated greatly. This can be due to the fact that the way CDE records this data differently from 2011.
  - Thus, we resample the data, using data from 2011 to 2015, and include only the schools that have records in all these years. We then apply the DiD model again on the resampled data. This analysis serves as a robustness test to the first regression.
  - We do a second robustness test with the resampled data. In this regression, we use a fixed effect model. The results are quite robust.
  - To visually identify the differences between treatment and control group and the changes over time, we also apply data visualization on both the entire dataset and the resampled data.
  - The codes are recorded in:
    - data5_regression_plots.py
    - plots_trends_of_outcomes.py
  - The plots are saved in the "plots" folder and the regression results are saved in "regression_results".

The ACS analysis serves as a background analysis in our project. We use annually county-level data of California's food business from ACS, clean them up and store them in the "data" folder:
- The codes for cleaning the datasets can be found in the "ACS_Food Business":
  - ACS_data1_cleaning.py
- The results are saved in "data" folder:
  - ACS_LA.csv
  - ACS_Agriculture.csv; ACS_FoodServices.csv; ACS_Retail.csv; ACS_Wholesale.csv
- We then use California's geometry data and ACS data to plot maps showing the trends of the growth of each business sector. The code can be found in "ACS_Food Business" folder:
  - ACS_GIS_CA2011.py
  - ACS_GIS_CA2016.py
  - The plots are saved in "plots" folders
- We also take the initiative to plot an interactive map using folium. The codes can be found as:
  - plots_folium.py


#### Deliverables and Presentation
Here, we list all of our deliverable available in this repository.
- We carefully analyze the results of our regression, also point out caveats and potential improvements of the project. The results, together with the visualization products are presented on our website: [IPPP Final Project: L.Liu, Y.Hao, M.Wang](https://lizhong-liu.github.io/GFPP_DiD/). (You can also find the codes of the website write-up in this root directory)
- Data files: longitude school-level data in .csv format (from 2004 to 2016).
- Sqlite database with all variables used in our regression.
- Data visualization products in "plots" folder, especially the maps of California county-level food business growth.


**Please refer to our website for more details!**


#### Reference
- [Tracking the Ripple Effects of LA’s Good Food Purchasing Program](http://www.policylink.org/equity-in-action/la-good-food-purchasing-program)
- [Healthy Food Procurement Policies and Their Impact](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3986994/)
- [Dietary effects of the National School Lunch Program and the School Breakfast Program](http://ajcn.nutrition.org/content/61/1/221S.full.pdf+html)
- [Evaluating the Impact of Conditional Cash Transfer Programs](https://academic.oup.com/wbro/article-abstract/20/1/29/1667806)
