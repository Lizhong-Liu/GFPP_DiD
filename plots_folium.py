import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
import geopandas as gpd
import pandas as pd
import folium

geo_df = gpd.read_file("data/CA_counties/CA_counties.shp", index='NAMELSAD')

files = ['ACS_Agriculture.csv', 'ACS_FoodServices.csv', 'ACS_Retail.csv', 'ACS_Wholesale.csv']
ft = []
for i in files:
    df = pd.read_csv('data/{}'.format(i), usecols = ['Unnamed: 0', 'ACS_11', 'ACS_15'])
    df.rename(columns = {'ACS_11': '{}-11'.format(i[4:-4]),
                         'ACS_15': '{}-15'.format(i[4:-4]),
                         'Unnamed: 0': 'NAMELSAD'}, inplace = True)
    ft.append('{}-11'.format(i[4:-4]))
    ft.append('{}-15'.format(i[4:-4]))
    df['NAMELSAD'] = [i.split(',')[0] for i in df['NAMELSAD']]
    geo_df = pd.merge(geo_df, df, on = 'NAMELSAD', how = 'inner')

geo_df.fillna(0, inplace = True)

m = folium.Map([37, -119],
               tiles='cartodbpositron',
               zoom_start=6, max_zoom=14, min_zoom=4)

folium.Marker([34.054, -118.244], popup='Los Angeles').add_to(m)
colormap = folium.LinearColormap(("orange", "white", "purple"),
                                 vmin = 0,
                                 vmax = 45000,
                                 caption = 'Employment in Food Business')
colormap.add_to(m)

ft = geo_df.columns[-8:]

for i in ft:
    m.add_child(folium.GeoJson(geo_df, name = i,
                               style_function = lambda feature: {
                               'fillColor': colormap(feature['properties'][i]),
                               "color" : "black", "weight" : 1, "fillOpacity" : 0.4}))

m.add_child(folium.LayerControl())
m.save("ca_agr.html")
