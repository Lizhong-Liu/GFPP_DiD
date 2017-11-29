{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "import glob\n",
    "import pandas as pd\n",
    "path = r'/Users/helenawang/Desktop/IPPP2017/final project/ACS_05-16'\n",
    "filenames = glob.glob(path +\"/*.csv\")\n",
    "\n",
    "ACS_05 = pd.read_csv(filenames[0],\n",
    "                     index_col = 1,\n",
    "                     usecols = [0,2,7,15,17,51],\n",
    "                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],\n",
    "                     skiprows=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_06 = pd.read_csv(filenames[1],\n",
    "                     index_col = 1,\n",
    "                     usecols = [0,2,7,15,17,51],\n",
    "                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],\n",
    "                     skiprows=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_07 = pd.read_csv(filenames[2],\n",
    "                     index_col = 1,\n",
    "                     usecols = [0,2,7,15,17,51],\n",
    "                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],\n",
    "                     skiprows=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_08 = pd.read_csv(filenames[3],\n",
    "                     index_col = 1,\n",
    "                     usecols = [0,2,7,15,17,51],\n",
    "                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],\n",
    "                     skiprows=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_09 = pd.read_csv(filenames[4],\n",
    "                     index_col = 1,\n",
    "                     usecols = [0,2,7,15,17,51],\n",
    "                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],\n",
    "                     skiprows=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_10 = pd.read_csv(filenames[5],\n",
    "                     index_col = 1,\n",
    "                     usecols = [0,2,7,15,17,51],\n",
    "                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],\n",
    "                     skiprows=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_11 = pd.read_csv(filenames[6],\n",
    "                     index_col = 1,\n",
    "                     usecols = [0,2,7,15,17,51],\n",
    "                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],\n",
    "                     skiprows=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_12 = pd.read_csv(filenames[7],\n",
    "                     index_col = 1,\n",
    "                     usecols = [0,2,7,15,17,51],\n",
    "                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],\n",
    "                     skiprows=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_13 = pd.read_csv(filenames[8],\n",
    "                     index_col = 1,\n",
    "                     usecols = [0,2,7,15,17,51],\n",
    "                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],\n",
    "                     skiprows=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_14 = pd.read_csv(filenames[9],\n",
    "                     index_col = 1,\n",
    "                     usecols = [0,2,7,15,17,51],\n",
    "                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],\n",
    "                     skiprows=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_15 = pd.read_csv(filenames[10],\n",
    "                     index_col = 1,\n",
    "                     usecols = [0,2,7,15,17,51],\n",
    "                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],\n",
    "                     skiprows=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_16 = pd.read_csv(filenames[11],\n",
    "                     index_col = 1,\n",
    "                     usecols = [0,2,7,15,17,51],\n",
    "                     names = ['ID','County Name','Agriculture','Wholesale','Retail','Food Services'],\n",
    "                     skiprows=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "Agriculture = pd.concat([ACS_05['Agriculture'],\n",
    "                         ACS_06['Agriculture'],\n",
    "                         ACS_07['Agriculture'],\n",
    "                         ACS_08['Agriculture'],\n",
    "                         ACS_09['Agriculture'],\n",
    "                         ACS_10['Agriculture'],\n",
    "                         ACS_11['Agriculture'],\n",
    "                         ACS_12['Agriculture'],\n",
    "                         ACS_13['Agriculture'],\n",
    "                         ACS_14['Agriculture'],\n",
    "                         ACS_15['Agriculture'],\n",
    "                         ACS_16['Agriculture']], \n",
    "                        keys=['ACS_05', 'ACS_06', 'ACS_07', 'ACS_08', 'ACS_09', 'ACS_10','ACS_11','ACS_12', 'ACS_13', 'ACS_14', 'ACS_15', 'ACS_16'],\n",
    "                        axis=1)\n",
    "Agriculture.to_csv('ACS_Agriculture.csv', sep=',')\n",
    "Agriculture_LA = Agriculture.loc['Los Angeles County, California'].to_frame('Agriculture')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "Wholesale = pd.concat([ACS_05['Wholesale'],\n",
    "                         ACS_06['Wholesale'],\n",
    "                         ACS_07['Wholesale'],\n",
    "                         ACS_08['Wholesale'],\n",
    "                         ACS_09['Wholesale'],\n",
    "                         ACS_10['Wholesale'],\n",
    "                         ACS_11['Wholesale'],\n",
    "                         ACS_12['Wholesale'],\n",
    "                         ACS_13['Wholesale'],\n",
    "                         ACS_14['Wholesale'],\n",
    "                         ACS_15['Wholesale'],\n",
    "                         ACS_16['Wholesale']], \n",
    "                      keys=['ACS_05', 'ACS_06', 'ACS_07', 'ACS_08', 'ACS_09', 'ACS_10','ACS_11','ACS_12', 'ACS_13', 'ACS_14', 'ACS_15', 'ACS_16'],\n",
    "                        axis=1)\n",
    "Wholesale.to_csv('ACS_Wholesale.csv', sep=',')\n",
    "Wholesale_LA = Wholesale.loc['Los Angeles County, California'].to_frame('Wholesale')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "Retail = pd.concat([ACS_05['Retail'],\n",
    "                         ACS_06['Retail'],\n",
    "                         ACS_07['Retail'],\n",
    "                         ACS_08['Retail'],\n",
    "                         ACS_09['Retail'],\n",
    "                         ACS_10['Retail'],\n",
    "                         ACS_11['Retail'],\n",
    "                         ACS_12['Retail'],\n",
    "                         ACS_13['Retail'],\n",
    "                         ACS_14['Retail'],\n",
    "                         ACS_15['Retail'],\n",
    "                         ACS_16['Retail']], \n",
    "                      keys=['ACS_05', 'ACS_06', 'ACS_07', 'ACS_08', 'ACS_09', 'ACS_10', 'ACS_11','ACS_12', 'ACS_13', 'ACS_14', 'ACS_15', 'ACS_16'],\n",
    "                        axis=1)\n",
    "Retail.to_csv('ACS_Retail.csv', sep=',')\n",
    "Retail_LA= Retail.loc['Los Angeles County, California'].to_frame('Retail')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "FoodServices = pd.concat([ACS_05['Food Services'],\n",
    "                         ACS_06['Food Services'],\n",
    "                         ACS_07['Food Services'],\n",
    "                         ACS_08['Food Services'],\n",
    "                         ACS_09['Food Services'],\n",
    "                         ACS_10['Food Services'],\n",
    "                         ACS_11['Food Services'],\n",
    "                         ACS_12['Food Services'],\n",
    "                         ACS_13['Food Services'],\n",
    "                         ACS_14['Food Services'],\n",
    "                         ACS_15['Food Services'],\n",
    "                         ACS_16['Food Services']], \n",
    "                      keys=['ACS_05', 'ACS_06', 'ACS_07', 'ACS_08', 'ACS_09', 'ACS_10', 'ACS_11','ACS_12', 'ACS_13', 'ACS_14', 'ACS_15', 'ACS_16'],\n",
    "                        axis=1)\n",
    "FoodServices.to_csv('ACS_FoodServices.csv', sep=',')\n",
    "FoodServices_LA = FoodServices.loc['Los Angeles County, California'].to_frame('FoodServices')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_LA = pd.concat([Agriculture_LA,Wholesale_LA,Retail_LA, FoodServices_LA], axis=1)\n",
    "ACS_LA.index.name = 'Year'\n",
    "ACS_LA.reset_index(level=0, inplace=True)\n",
    "ACS_LA.to_csv('ACS_LA.csv', sep=',')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_LA.plot(x=\"Year\",y=\"Agriculture\",kind='bar')\n",
    "plt.ylabel('Number of Employment')\n",
    "plt.yticks(np.arange(0,30000,5000))\n",
    "plt.xlabel('Year')\n",
    "plt.title('Number of Employment in Agriculture Industry from 2005 to 2016')\n",
    "plt.savefig('Agriculture_LA')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_LA.plot(x=\"Year\",y=\"Wholesale\",kind='bar')\n",
    "plt.ylabel('Number of Employment')\n",
    "plt.yticks(np.arange(100000,300000,50000))\n",
    "plt.xlabel('Year')\n",
    "plt.title('Number of Employment in Wholesale Industry from 2005 to 2016')\n",
    "plt.savefig('Wholesale_LA')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_LA.plot(x=\"Year\",y=\"Retail\",kind='bar')\n",
    "plt.ylabel('Number of Employment')\n",
    "plt.yticks(np.arange(0,750000,100000))\n",
    "plt.xlabel('Year')\n",
    "plt.title('Number of Employment in Retail Industry from 2005 to 2016')\n",
    "plt.savefig('Retail_LA')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_LA.plot(x=\"Year\",y=\"FoodServices\",kind='bar')\n",
    "plt.ylabel('Number of Employment')\n",
    "plt.yticks(np.arange(0,500000,50000))\n",
    "plt.xlabel('Year')\n",
    "plt.title('Number of Employment in Food Services Industry from 2005 to 2016')\n",
    "plt.savefig('FoodServices_LA')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACS_LA.plot(x=\"Year\",y=['Agriculture','Wholesale','Retail',\"FoodServices\"])\n",
    "plt.ylabel('Number of Employment')\n",
    "plt.xlabel('Year')\n",
    "plt.title('Number of Employment in Food Related Industry from 2005 to 2016')\n",
    "plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))\n",
    "plt.savefig('ACS_LA')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
