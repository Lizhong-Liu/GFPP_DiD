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
- Health:
  - [Physical Fitness (California Department of Education (CDE))](https://www.cde.ca.gov/ta/tg/pf/pftresearch.asp)
Independent variables:
- School Demographics:
  - [Enrollment (CDE)](https://www.cde.ca.gov/ds/sd/sd/filesenr.asp);
  - [Demographics (CDE)](https://www.cde.ca.gov/ds/sd/sd/filesenr.asp);
- Household Economic Development:
  - [School-level Poverty Rate (CDE)](https://www.cde.ca.gov/ds/sd/sd/filessp.asp);
  - [Employment & Industry (American Community Survey (ACS))](https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml?refresh=t)

Besides regressional analysis, we also want to examine the potential influence of GFPP on LA's local food business. Unfortunately, for now there is little available micro-level data on it, so we cannot include it in our regression model. Instead, we use American Community Survey data on county level and plot an interactive map to show the growth of different food-related sectors (including Agriculture, Food Services, Retail, and Wholesale). The source of data can be found via this [link]()
  
  
#### Reference
- [Tracking the Ripple Effects of LA’s Good Food Purchasing Program](http://www.policylink.org/equity-in-action/la-good-food-purchasing-program)
- [Healthy Food Procurement Policies and Their Impact](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3986994/)
- [Dietary effects of the National School Lunch Program and the School Breakfast Program](http://ajcn.nutrition.org/content/61/1/221S.full.pdf+html)
- [Evaluating the Impact of Conditional Cash Transfer Programs](https://academic.oup.com/wbro/article-abstract/20/1/29/1667806)
  
#### Timeline
  
  
  | Task                           | Sub-task                   | Responsible Team Member | Deadline |
  | ------------------------------ | -------------------------- | ----------------------- | -------- |
  | 1. Proposal Draft              | README and submission      | Lizhong                 | Oct 31   |
  |                                | Formatting                 | Manyi                   | Oct 31   |
  |                                | Statsmodel                 | Yiran                   | Oct 31   |
  | 2. Background Research         | Data sources               | All                     | Nov 7    |
  |                                | Literature Review          | All                     | Nov 7    |
  | 3. Data Processing             | Data Cleaning and Analysis | All                     | Nov 14   |
  |                                | Data Visualization         | All                     | Nov 21   |
  | 4. Report Writing/Presentation |                            | All                     | Dec 1    |
