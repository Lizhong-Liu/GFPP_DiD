
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd


# In[2]:


counties = gpd.read_file("CA_counties/CA_counties.shp")
counties["Counties"] = counties["NAMELSAD"]
counties = counties.set_index("Counties")
counties.plot().set_axis_off()


# In[3]:


Agriculture_CA = pd.read_csv("ACS_Agriculture.csv")
Agriculture_CA.rename(columns={'Unnamed: 0': 'Counties'}, inplace=True)
Agriculture_CA["Counties"] = Agriculture_CA["Counties"].str.replace(r'\, California','')
Agriculture_CA_16 = Agriculture_CA [['Counties','ACS_16']].set_index( "Counties")


# In[4]:


Retail_CA = pd.read_csv("ACS_Retail.csv")
Retail_CA.rename(columns={'Unnamed: 0': 'Counties'}, inplace=True)
Retail_CA["Counties"] = Retail_CA["Counties"].str.replace(r'\, California','')
Retail_CA_16 = Retail_CA [['Counties','ACS_16']].set_index( "Counties")


# In[5]:


Wholesale_CA = pd.read_csv("ACS_Wholesale.csv")
Wholesale_CA.rename(columns={'Unnamed: 0': 'Counties'}, inplace=True)
Wholesale_CA["Counties"] = Wholesale_CA["Counties"].str.replace(r'\, California','')
Wholesale_CA_16 = Wholesale_CA [['Counties','ACS_16']].set_index( "Counties")


# In[6]:


FoodServices_CA = pd.read_csv("ACS_FoodServices.csv")
FoodServices_CA.rename(columns={'Unnamed: 0': 'Counties'}, inplace=True)
FoodServices_CA["Counties"] = FoodServices_CA["Counties"].str.replace(r'\, California','')
FoodServices_CA_16 = FoodServices_CA [['Counties','ACS_16']].set_index( "Counties")


# In[7]:


merged_Agr = counties.join(Agriculture_CA_16, how = "inner")
magri = merged_Agr.to_crs(epsg = 2225).plot(column = "ACS_16", cmap = "Blues",
                                     edgecolor = "grey", figsize = (5,5),legend = True,k=10)
magri.set_title('Number of Agriculture Related Business in California 2016', fontsize = 10, y = 1.15)
magri.set_axis_off()
plt.savefig('plots/GIS_Agriculture_16.pdf')


# In[8]:


merged_Ret = counties.join(Retail_CA_16, how = "inner")
mret = merged_Ret.to_crs(epsg = 2225).plot(column = "ACS_16", cmap = "Greens",
                                     edgecolor = "grey", figsize = (5, 5),legend = True,k=10)
mret.set_title('Number of Retail Related Business in California 2016', fontsize = 10, y = 1.15)
mret.set_axis_off()
plt.savefig('plots/GIS_Retail_16.pdf')


# In[9]:


merged_Who = counties.join(Wholesale_CA_16, how = "inner")
mwho = merged_Who.to_crs(epsg = 2225).plot(column = "ACS_16", cmap = "Reds",
                                     edgecolor = "grey", figsize = (5, 5),legend = True,k=10)
mwho.set_title('Number of Wholesale Related Business in California 2016', fontsize = 10, y = 1.15)
mwho.set_axis_off()
plt.savefig('plots/GIS_Wholesale_16.pdf')


# In[12]:


merged_Fs = counties.join(FoodServices_CA_16, how = "inner")
mfs = merged_Fs.to_crs(epsg = 2225).plot(column = "ACS_16", cmap = "Purples",
                                     edgecolor = "grey", figsize = (5, 5),legend = True,k=10)
mfs.set_title('Number of Food Services Related Business in California 2016', fontsize = 10, y = 1.15)
mfs.set_axis_off()
plt.savefig('plots/GIS_FoodServices_16.pdf')
