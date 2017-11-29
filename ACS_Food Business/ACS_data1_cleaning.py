
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


import glob
import pandas as pd
path = r'/Users/helenawang/Desktop/IPPP2017/final project/ACS_05-16'
filenames = glob.glob(path +"/*.csv")

ACS_05 = pd.read_csv(filenames[0],
                     index_col = 1,
                     usecols = [0,2,7,15,17,51],
                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],
                     skiprows=2)


# In[3]:


ACS_06 = pd.read_csv(filenames[1],
                     index_col = 1,
                     usecols = [0,2,7,15,17,51],
                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],
                     skiprows=2)


# In[4]:


ACS_07 = pd.read_csv(filenames[2],
                     index_col = 1,
                     usecols = [0,2,7,15,17,51],
                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],
                     skiprows=2)


# In[5]:


ACS_08 = pd.read_csv(filenames[3],
                     index_col = 1,
                     usecols = [0,2,7,15,17,51],
                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],
                     skiprows=2)


# In[6]:


ACS_09 = pd.read_csv(filenames[4],
                     index_col = 1,
                     usecols = [0,2,7,15,17,51],
                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],
                     skiprows=2)


# In[7]:


ACS_10 = pd.read_csv(filenames[5],
                     index_col = 1,
                     usecols = [0,2,7,15,17,51],
                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],
                     skiprows=2)


# In[8]:


ACS_11 = pd.read_csv(filenames[6],
                     index_col = 1,
                     usecols = [0,2,7,15,17,51],
                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],
                     skiprows=2)


# In[9]:


ACS_12 = pd.read_csv(filenames[7],
                     index_col = 1,
                     usecols = [0,2,7,15,17,51],
                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],
                     skiprows=2)


# In[10]:


ACS_13 = pd.read_csv(filenames[8],
                     index_col = 1,
                     usecols = [0,2,7,15,17,51],
                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],
                     skiprows=2)


# In[11]:


ACS_14 = pd.read_csv(filenames[9],
                     index_col = 1,
                     usecols = [0,2,7,15,17,51],
                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],
                     skiprows=2)


# In[12]:


ACS_15 = pd.read_csv(filenames[10],
                     index_col = 1,
                     usecols = [0,2,7,15,17,51],
                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],
                     skiprows=2)


# In[13]:


ACS_16 = pd.read_csv(filenames[11],
                     index_col = 1,
                     usecols = [0,2,7,15,17,51],
                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],
                     skiprows=2)


# In[14]:


Agriculture = pd.concat([ACS_05['Agriculture'],
                         ACS_06['Agriculture'],
                         ACS_07['Agriculture'],
                         ACS_08['Agriculture'],
                         ACS_09['Agriculture'],
                         ACS_10['Agriculture'],
                         ACS_11['Agriculture'],
                         ACS_12['Agriculture'],
                         ACS_13['Agriculture'],
                         ACS_14['Agriculture'],
                         ACS_15['Agriculture'],
                         ACS_16['Agriculture']],
                        keys=['ACS_05', 'ACS_06', 'ACS_07', 'ACS_08', 'ACS_09', 'ACS_10','ACS_11','ACS_12', 'ACS_13', 'ACS_14', 'ACS_15', 'ACS_16'],
                        axis=1)
Agriculture.to_csv('data/ACS_Agriculture.csv', sep=',')
Agriculture_LA = Agriculture.loc['Los Angeles County, California'].to_frame('Agriculture')


# In[15]:


Wholesale = pd.concat([ACS_05['Wholesale'],
                         ACS_06['Wholesale'],
                         ACS_07['Wholesale'],
                         ACS_08['Wholesale'],
                         ACS_09['Wholesale'],
                         ACS_10['Wholesale'],
                         ACS_11['Wholesale'],
                         ACS_12['Wholesale'],
                         ACS_13['Wholesale'],
                         ACS_14['Wholesale'],
                         ACS_15['Wholesale'],
                         ACS_16['Wholesale']],
                      keys=['ACS_05', 'ACS_06', 'ACS_07', 'ACS_08', 'ACS_09', 'ACS_10','ACS_11','ACS_12', 'ACS_13', 'ACS_14', 'ACS_15', 'ACS_16'],
                        axis=1)
Wholesale.to_csv('data/ACS_Wholesale.csv', sep=',')
Wholesale_LA = Wholesale.loc['Los Angeles County, California'].to_frame('Wholesale')


# In[16]:


Retail = pd.concat([ACS_05['Retail'],
                         ACS_06['Retail'],
                         ACS_07['Retail'],
                         ACS_08['Retail'],
                         ACS_09['Retail'],
                         ACS_10['Retail'],
                         ACS_11['Retail'],
                         ACS_12['Retail'],
                         ACS_13['Retail'],
                         ACS_14['Retail'],
                         ACS_15['Retail'],
                         ACS_16['Retail']],
                      keys=['ACS_05', 'ACS_06', 'ACS_07', 'ACS_08', 'ACS_09', 'ACS_10', 'ACS_11','ACS_12', 'ACS_13', 'ACS_14', 'ACS_15', 'ACS_16'],
                        axis=1)
Retail.to_csv('data/ACS_Retail.csv', sep=',')
Retail_LA= Retail.loc['Los Angeles County, California'].to_frame('Retail')


# In[17]:


FoodServices = pd.concat([ACS_05['Food Services'],
                         ACS_06['Food Services'],
                         ACS_07['Food Services'],
                         ACS_08['Food Services'],
                         ACS_09['Food Services'],
                         ACS_10['Food Services'],
                         ACS_11['Food Services'],
                         ACS_12['Food Services'],
                         ACS_13['Food Services'],
                         ACS_14['Food Services'],
                         ACS_15['Food Services'],
                         ACS_16['Food Services']],
                      keys=['ACS_05', 'ACS_06', 'ACS_07', 'ACS_08', 'ACS_09', 'ACS_10', 'ACS_11','ACS_12', 'ACS_13', 'ACS_14', 'ACS_15', 'ACS_16'],
                        axis=1)
FoodServices.to_csv('data/ACS_FoodServices.csv', sep=',')
FoodServices_LA = FoodServices.loc['Los Angeles County, California'].to_frame('FoodServices')


# In[40]:


ACS_LA = pd.concat([Agriculture_LA,Wholesale_LA,Retail_LA, FoodServices_LA], axis=1)
ACS_LA.index.name = 'Year'
ACS_LA.reset_index(level=0, inplace=True)
ACS_LA[['Agr_IR','Who_IR','Ret_IR','Fds_IR']]=ACS_LA[['Agriculture','Wholesale','Retail','FoodServices']].pct_change()
ACS_LA.to_csv('data/ACS_LA.csv', sep=',')


# In[19]:


ACS_LA.plot(x="Year",y="Agriculture",kind='bar')
plt.ylabel('Number of Employment')
plt.yticks(np.arange(0,30000,5000))
plt.xlabel('Year')
plt.title('Number of Employment in Agriculture Industry from 2005 to 2016')
plt.savefig('plots/Agriculture_LA.pdf')


# In[20]:


ACS_LA.plot(x="Year",y="Wholesale",kind='bar')
plt.ylabel('Number of Employment')
plt.yticks(np.arange(100000,300000,50000))
plt.xlabel('Year')
plt.title('Number of Employment in Wholesale Industry from 2005 to 2016')
plt.savefig('plots/Wholesale_LA.pdf')


# In[21]:


ACS_LA.plot(x="Year",y="Retail",kind='bar')
plt.ylabel('Number of Employment')
plt.yticks(np.arange(0,750000,100000))
plt.xlabel('Year')
plt.title('Number of Employment in Retail Industry from 2005 to 2016')
plt.savefig('plots/Retail_LA.pdf')


# In[22]:


ACS_LA.plot(x="Year",y="FoodServices",kind='bar')
plt.ylabel('Number of Employment')
plt.yticks(np.arange(0,500000,50000))
plt.xlabel('Year')
plt.title('Number of Employment in Food Services Industry from 2005 to 2016')
plt.savefig('plots/FoodServices_LA.pdf')


# In[39]:


ACS_LA.plot(x="Year",y=['Agriculture','Wholesale','Retail',"FoodServices"])
plt.ylabel('Number of Employment')
plt.xlabel('Year')
plt.title('Number of Employment in Food Related Industry from 2005 to 2016')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('plots/ACS_LA.pdf')


# In[64]:


ax=ACS_LA.plot(x="Year",y=['Agr_IR','Who_IR','Ret_IR','Fds_IR'])
plt.ylabel('Employment Increasing Rate')
plt.xlabel('Year')
plt.title('Employment Increasing Rate in Food Related Industries from 2005 to 2016',y=1.1)

major_ticks = np.arange(-0.5, 1, 0.5)
ax.set_yticks(major_ticks)

ax.grid(which='both')

# or if you want differnet settings for the grids:
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.axvspan(6, 11, alpha=0.1, color='red')
plt.savefig('plots/ACS_LA_IR.pdf')
