# Good Food Purchasing Program in LA: Socio-economic Impacts and Implications
## PPHA 30550/1 - Final Project
**Group Member: [Manyi Wang](@manyiw), [Yiran Hao](@chiertu), [Lizhong Liu](@Lizhong-Liu)**


#### GFPP Overview
Good Food Purchasing Program (GFPP) is an initiative currently implemented in several municipalities such as Los Angeles, San Francisco, and New York, which is mainly adopted by public institutions (public schools, municipalities, etc.). The bodies practicing such program restrict their purchase of meals by standards of nutrition, of raw material sources, and of envrionmental influences. GFPP has five value criteria: animal welfare, nutrition, support for local business, rights of employees (such as safety and justice), and environmental sustainability. 

A more insightful overview of GFPP can be found on the website of [Center for Good Food Purchasing](https://goodfoodpurchasing.org/program-overview/). You can also find details of LA's GFPP practice [here](http://goodfoodla.org/good-food/) and [here](https://achieve.lausd.net/Page/11672).


#### Project Goals
Our project aims to identify the causal relations between the implementation of this program and local socio-economic development by applying a Difference-in-difference analysis. Since Los Angeles is the very first city piloting the program, we mark LA as our "city of interest". Given that LA adopted the policy from 2012, our timeframe and sample size are limited, we will also include San Francisco -- the second city adopting the policy -- into our sample.

The City of Chicago has just adopted GFPP in this Octorber. Therefore, we will also try to further utilize our regression results to induce the implications of adopting GFPP to the socio-economic development of Chicago.


#### Deliverables
The following list exhibits potential deliverables of our project:
- Descriptive analysis of the socio-economic development level of Los Angeles;
- Difference-in-Difference results (presented in tables), including baseline regression results and discontinuity regression results;
- Data visualization of the baseline regressions and the DiD results;
- Mapping of the school district adopting GFPP throughout LA, together with the income level (suggesting with different shades).


#### Variables and Data Source
Our model tries to test the potential impacts of GFPP on mutiple socio-economic indicators: health, human capital (education), and household economic development. Within these three categories, we further specify the variables as following:
- Health:
  - [Children Food Security Data (Los Angeles Health Department (LAHD))](http://www.publichealth.lacounty.gov/ha/HA_DATA_TRENDS.htm#Child);
  - [Physical Fitness](https://www.cde.ca.gov/ta/tg/pf/pftresearch.asp)
- School Demographics:
  - [Enrollment](https://www.cde.ca.gov/ds/sd/sd/filesenr.asp);
  - [Demographics](https://www.cde.ca.gov/ds/sd/sd/filesenr.asp);
- Household Economic Development:
  - [School-level Poverty Rate](https://www.cde.ca.gov/ds/sd/sd/filessp.asp);
  - [Employment & Industry](https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml?refresh=t)
- Other Socio-Economic indicators:
  As GFPP also intends to support the development of local business, we also want to test its effects on helping local business thrive. We propose to use [Active Businesses data](https://data.lacity.org/A-Prosperous-City/Listing-of-Active-Businesses/6rrh-rzua) and focus on the increments of businesses (especially those in food industry) before and after GFPP's adoptation.
  
  
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
