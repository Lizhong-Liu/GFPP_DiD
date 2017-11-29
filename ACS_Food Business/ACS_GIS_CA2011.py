
# coding: utf-8

# In[9]:


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd


# In[10]:


counties = gpd.read_file("CA_counties/CA_counties.shp")
counties["Counties"] = counties["NAMELSAD"]
counties = counties.set_index("Counties")
counties.plot().set_axis_off()


# In[11]:


Agriculture_CA = pd.read_csv("ACS_Agriculture.csv")
Agriculture_CA.rename(columns={'Unnamed: 0': 'Counties'}, inplace=True)

Agriculture_CA["Counties"] = Agriculture_CA["Counties"].str.replace(r'\, California','')
Agriculture_CA_11 = Agriculture_CA [['Counties','ACS_11']].set_index( "Counties")


# In[12]:


Retail_CA = pd.read_csv("ACS_Retail.csv")
Retail_CA.rename(columns={'Unnamed: 0': 'Counties'}, inplace=True)
Retail_CA["Counties"] = Retail_CA["Counties"].str.replace(r'\, California','')
Retail_CA_11 = Retail_CA [['Counties','ACS_11']].set_index( "Counties")


# In[13]:


Wholesale_CA = pd.read_csv("ACS_Wholesale.csv")
Wholesale_CA.rename(columns={'Unnamed: 0': 'Counties'}, inplace=True)
Wholesale_CA["Counties"] = Wholesale_CA["Counties"].str.replace(r'\, California','')
Wholesale_CA_11 = Wholesale_CA [['Counties','ACS_11']].set_index( "Counties")


# In[14]:


FoodServices_CA = pd.read_csv("ACS_FoodServices.csv")
FoodServices_CA.rename(columns={'Unnamed: 0': 'Counties'}, inplace=True)
FoodServices_CA["Counties"] = FoodServices_CA["Counties"].str.replace(r'\, California','')
FoodServices_CA_11 = FoodServices_CA [['Counties','ACS_11']].set_index( "Counties")


# In[15]:


merged_Agr = counties.join(Agriculture_CA_11, how = "inner")
magri = merged_Agr.to_crs(epsg = 2225).plot(column = "ACS_11", cmap = "Blues",
                                     edgecolor = "grey", figsize = (5,5),legend = True,k=10)
magri.set_title('Number of Agriculture Related Business in California 2011', fontsize = 10, y = 1.15)
magri.set_axis_off()
plt.savefig('plots/GIS_Agriculture_11.pdf')


# In[16]:


merged_Ret = counties.join(Retail_CA_11, how = "inner")
mret = merged_Ret.to_crs(epsg = 2225).plot(column = "ACS_11", cmap = "Greens",
                                     edgecolor = "grey", figsize = (5, 5),legend = True,k=10)
mret.set_title('Number of Retail Related Business in California 2011', fontsize = 10, y = 1.15)
mret.set_axis_off()
plt.savefig('plots/GIS_Retail_11.pdf')


# In[17]:


merged_Who = counties.join(Wholesale_CA_11, how = "inner")
mwho = merged_Who.to_crs(epsg = 2225).plot(column = "ACS_11", cmap = "Reds",
                                     edgecolor = "grey", figsize = (5, 5),legend = True,k=10)
mwho.set_title('Number of Wholesale Related Business in California 2011', fontsize = 10, y = 1.15)
mwho.set_axis_off()
plt.savefig('plots/GIS_Wholesale_11.pdf')


# In[18]:


merged_Fs = counties.join(FoodServices_CA_11, how = "inner")
mfs = merged_Fs.to_crs(epsg = 2225).plot(column = "ACS_11", cmap = "Purples",
                                     edgecolor = "grey", figsize = (5, 5),legend = True,k=10)
mfs.set_title('Number of Food Services Related Business in California 2011', fontsize = 10, y = 1.15)
mfs.set_axis_off()
plt.savefig('plots/GIS_FoodServices_11.pdf')
