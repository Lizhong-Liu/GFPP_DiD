# Transit2Home
## PPHA 30550/1 - Final Project
**Group Member: [Manyi Wang](@manyiw), [Yiran Hao](@chiertu), [Lizhong Liu](@Lizhong-Liu)**


#### Project Overview
We will develop an interactive website for the homeless and organizations (e.g. [Cardborigami](http://www.cardborigami.org)) building temporary shelters for the homeless by mapping current shelters and potential locations for new shelters. We will use open data of Chicago and pilot in Chicago. Once the feasibility proves out, we will promote the projects to major cities including New York City, Washington DC, Los Angeles, and San Francisco etc. 


#### Policy Interest: Urban Planning, Social Work and Public Administration
- Provide references for the government and nonprofits to help the homeless
- Inform the public of locations where the homeless gather and loiter
- Better utilize public resources
- To be continued...

  **We will present the potential benefits of the project by studying correlations between the following pairs of variables**
  - crime rates vs. density of the homeless
  - environmental factors vs. income level
  - ...
  
  
#### Data Source
Ideal shelter sites should provide a habitable and convenient living environment for the homeless and at the same time cause little disturbance to surrounding neighborhood. To achieve this goal, we selected three site selection criteria that we think best reflect the needs of both sides. The three criteria, with their respetive data source in hyperlink, are listed below into two categories, geographical and socioeconomic. We also list some tentative criteria that we think are relevant but could not make it to our criteria due to lack of data.

- Our geographical criteria are:
  - Land should be open and level and ideally have shield against sunlight or rain (we are mainly aiming at public parks and airport):
    - Data Source: ["Chicago Park District Facilities"](https://data.cityofchicago.org/Parks-Recreation/Parks-Chicago-Park-District-Facilities-current-/5yyk-qt9y) has the coordinates of Chicago park areas;
  - Tentative criteria:   
    - Elevation should be above level reachable by flooding rain or melting snow;
    - Noise level should be less than (a certain level);
    - Wind speed should be within a reasonable range;
    - ...

- Our socioeconomic criteria are:
  - Criminal activities should be at a low level:
    - Data Source: ["Crimes - 2001 to present"](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2/data) has the coordinates of Chicago crime activities;
  - Proximity to hospitals and medical helps:
    - Data Source: ["Hospitals - Chicago"](https://data.cityofchicago.org/Health-Human-Services/Hospitals-Chicago/ucpz-2r55) has the coordinates of Chicago hospitals;
  - Tentative criteria:
    - Historical or touristic sites should be avoided;
    - Population density is within a reasonable range;
    - ...

We will use the coordinates from these three sources to map out areas that:
- are located in green open space;
- are within certain range from the nearest hospital;
- have low level of criminal activities.
These areas will be the candidates for our shelter site locations.
  
  
#### Functionality of Transit2Home
- Exhibit the correlations between environmental resources and socioeconomic resources
- Exhibit locations where the homeless gather and loiter
- Mapping these locations suitable for the construction of temporary shelters
- Suggesting locations that are both suitable and lawful to build temporary locations
  
  
#### Visualization of Transit2Home
  We are going to develop an interactive website on which we intend to include (and potentially not limit to) the following:
- Neighborhoods and/or communities (boundaries); Demographical characteristics
- Open space: green space, parks, public recreational areas, rivers
- Economic development status: income level, GDP per capita
- Pins of the current available homeless shelters
- Pins of potential locations for the homeless
  
  
#### Potential Client
- Government
- Organizations with missions related to helping the homeless or building temporary shelters
- Researchers
- Other concerned parties
  
  
#### Reference
- [Current Shelters in Chicago](https://www.cityofchicago.org/city/en/depts/fss/provdrs/emerg/svcs/shelter_system.html)
- [Homeless Outreach in Chicago](https://www.cityofchicago.org/city/en/depts/fss/supp_info/homeless_outreachandengagement.html)
  
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
  | 5. Website Construction        |                            | All                     | Dec 4    |
