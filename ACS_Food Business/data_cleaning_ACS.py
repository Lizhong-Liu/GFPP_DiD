{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {
    "collapsed": true
   },
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
   "execution_count": 183,
   "metadata": {
    "collapsed": true
   },
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
   "execution_count": 184,
   "metadata": {
    "collapsed": true
   },
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
   "execution_count": 185,
   "metadata": {
    "collapsed": true
   },
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
   "execution_count": 186,
   "metadata": {
    "collapsed": true
   },
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
   "execution_count": 187,
   "metadata": {
    "collapsed": true
   },
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
   "execution_count": 188,
   "metadata": {
    "collapsed": true
   },
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
   "execution_count": 189,
   "metadata": {
    "collapsed": true
   },
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
   "execution_count": 190,
   "metadata": {
    "collapsed": true
   },
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
   "execution_count": 191,
   "metadata": {
    "collapsed": true
   },
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
   "execution_count": 192,
   "metadata": {
    "collapsed": true
   },
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
   "execution_count": 193,
   "metadata": {
    "collapsed": true
   },
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
   "execution_count": 194,
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
    "                        keys=['ACS_05', 'ACS_06', 'ACS_07', 'ACS_08', 'ACS_09', 'ACS_10', 'ACS_12', 'ACS_13', 'ACS_14', 'ACS_15', 'ACS_16'],\n",
    "                        axis=1)\n",
    "Agriculture_LA = Agriculture.loc['Los Angeles County, California'].to_frame('Agriculture')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
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
    "                      keys=['ACS_05', 'ACS_06', 'ACS_07', 'ACS_08', 'ACS_09', 'ACS_10', 'ACS_12', 'ACS_13', 'ACS_14', 'ACS_15', 'ACS_16'],\n",
    "                        axis=1)\n",
    "Wholesale_LA = Wholesale.loc['Los Angeles County, California'].to_frame('Wholesale')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
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
    "                      keys=['ACS_05', 'ACS_06', 'ACS_07', 'ACS_08', 'ACS_09', 'ACS_10', 'ACS_12', 'ACS_13', 'ACS_14', 'ACS_15', 'ACS_16'],\n",
    "                        axis=1)\n",
    "Retail_LA= Retail.loc['Los Angeles County, California'].to_frame('Retail')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
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
    "                      keys=['ACS_05', 'ACS_06', 'ACS_07', 'ACS_08', 'ACS_09', 'ACS_10', 'ACS_12', 'ACS_13', 'ACS_14', 'ACS_15', 'ACS_16'],\n",
    "                        axis=1)\n",
    "FoodServices_LA = FoodServices.loc['Los Angeles County, California'].to_frame('FoodServices')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Year</th>\n",
       "      <th>Agriculture</th>\n",
       "      <th>Wholesale</th>\n",
       "      <th>Retail</th>\n",
       "      <th>FoodServices</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ACS_05</td>\n",
       "      <td>10509.0</td>\n",
       "      <td>193331.0</td>\n",
       "      <td>460548.0</td>\n",
       "      <td>278482.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ACS_06</td>\n",
       "      <td>9879.0</td>\n",
       "      <td>201425.0</td>\n",
       "      <td>488499.0</td>\n",
       "      <td>296362.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ACS_07</td>\n",
       "      <td>10751.0</td>\n",
       "      <td>174599.0</td>\n",
       "      <td>481327.0</td>\n",
       "      <td>316034.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ACS_08</td>\n",
       "      <td>13607.0</td>\n",
       "      <td>180565.0</td>\n",
       "      <td>509493.0</td>\n",
       "      <td>309083.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ACS_09</td>\n",
       "      <td>19139.0</td>\n",
       "      <td>160758.0</td>\n",
       "      <td>466810.0</td>\n",
       "      <td>312008.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>ACS_10</td>\n",
       "      <td>21660.0</td>\n",
       "      <td>159909.0</td>\n",
       "      <td>468911.0</td>\n",
       "      <td>310310.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>ACS_12</td>\n",
       "      <td>21508.0</td>\n",
       "      <td>162179.0</td>\n",
       "      <td>470340.0</td>\n",
       "      <td>316086.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>ACS_13</td>\n",
       "      <td>17120.0</td>\n",
       "      <td>161787.0</td>\n",
       "      <td>483645.0</td>\n",
       "      <td>326664.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>ACS_14</td>\n",
       "      <td>19579.0</td>\n",
       "      <td>162638.0</td>\n",
       "      <td>503655.0</td>\n",
       "      <td>350197.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>ACS_15</td>\n",
       "      <td>21762.0</td>\n",
       "      <td>165783.0</td>\n",
       "      <td>508530.0</td>\n",
       "      <td>378430.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>ACS_16</td>\n",
       "      <td>23133.0</td>\n",
       "      <td>164029.0</td>\n",
       "      <td>509564.0</td>\n",
       "      <td>378681.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Year  Agriculture  Wholesale    Retail  FoodServices\n",
       "0   ACS_05      10509.0   193331.0  460548.0      278482.0\n",
       "1   ACS_06       9879.0   201425.0  488499.0      296362.0\n",
       "2   ACS_07      10751.0   174599.0  481327.0      316034.0\n",
       "3   ACS_08      13607.0   180565.0  509493.0      309083.0\n",
       "4   ACS_09      19139.0   160758.0  466810.0      312008.0\n",
       "5   ACS_10      21660.0   159909.0  468911.0      310310.0\n",
       "6   ACS_12      21508.0   162179.0  470340.0      316086.0\n",
       "7   ACS_13      17120.0   161787.0  483645.0      326664.0\n",
       "8   ACS_14      19579.0   162638.0  503655.0      350197.0\n",
       "9   ACS_15      21762.0   165783.0  508530.0      378430.0\n",
       "10  ACS_16      23133.0   164029.0  509564.0      378681.0"
      ]
     },
     "execution_count": 198,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ACS_LA = pd.concat([Agriculture_LA,Wholesale_LA,Retail_LA, FoodServices_LA], axis=1)\n",
    "ACS_LA.index.name = 'Year'\n",
    "ACS_LA.reset_index(level=0, inplace=True)\n",
    "ACS_LA.to_csv('ACS_LA.csv', sep=',')\n",
    "ACS_LA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 199,
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
   "execution_count": 200,
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
   "execution_count": 201,
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
   "execution_count": 202,
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
   "execution_count": 203,
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
   "metadata": {
    "collapsed": true
   },
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
   "version": "3.6.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
