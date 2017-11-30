#!/usr/bin/env python

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
    df['NAMELSAD'] = [i.split(',')[0] for i in df['NAMELSAD']]
    geo_df = pd.merge(geo_df, df, on = 'NAMELSAD', how = 'inner')

geo_df.fillna(0, inplace = True)

name = ['Agriculture', 'Food Services', 'Retail', 'Wholesale']
ft = geo_df.columns[-8:]
la = [i for i in geo_df.iloc[29, :][-8:]]
max_em = [geo_df['{}'.format(i)].max() for i in ft]
max_formap = [max_em[i] for i in range(1,len(max_em),2)]

# Folium mapping.
m = folium.Map([37, -119],
               tiles='cartodbpositron',
               zoom_start=6, max_zoom=14, min_zoom=4)

# Agriculture
folium.Marker([34.054, -118.244], popup='Los Angeles - 2011: {}, 2015: {}'.format(la[0], la[1])).add_to(m)
colormap1 = folium.LinearColormap(("white", "purple"),
                                    vmin = 0,
                                    vmax = max_formap[0],
                                    caption = 'Employment in {}'.format(name[0]))
colormap1.add_to(m)
for c in ft[:2]:
    folium.GeoJson(geo_df, name = c,
                   style_function = lambda feature: {
                   "fillColor": colormap1(feature["properties"][c]),
                   "color" : "black", "weight" : 1, "fillOpacity" : 0.4}).add_to(m)

# Food Services
folium.Marker([34.054, -118.244], popup='Los Angeles - 2011: {}, 2015: {}'.format(la[2], la[3])).add_to(m)
colormap2 = folium.LinearColormap(("white", "orange"),
                                    vmin = 0,
                                    vmax = max_formap[1],
                                    caption = 'Employment in {}'.format(name[1]))
colormap2.add_to(m)
for c in ft[2:4]:
    folium.GeoJson(geo_df, name = c,
                   style_function = lambda feature: {
                   "fillColor": colormap2(feature["properties"][c]),
                   "color" : "black", "weight" : 1, "fillOpacity" : 0.4}).add_to(m)

# Retail
folium.Marker([34.054, -118.244], popup='Los Angeles - 2011: {}, 2015: {}'.format(la[4], la[5])).add_to(m)
colormap3 = folium.LinearColormap(("white", "red"),
                                    vmin = 0,
                                    vmax = max_formap[2],
                                    caption = 'Employment in {}'.format(name[2]))
colormap3.add_to(m)
for c in ft[4:6]:
    folium.GeoJson(geo_df, name = c,
                   style_function = lambda feature: {
                   "fillColor": colormap3(feature["properties"][c]),
                   "color" : "black", "weight" : 1, "fillOpacity" : 0.4}).add_to(m)

# Wholesale
folium.Marker([34.054, -118.244], popup='Los Angeles - 2011: {}, 2015: {}'.format(la[6], la[7])).add_to(m)
colormap4 = folium.LinearColormap(("white", "blue"),
                                    vmin = 0,
                                    vmax = max_formap[3],
                                    caption = 'Employment in {}'.format(name[3]))
colormap4.add_to(m)
for c in ft[6:]:
    folium.GeoJson(geo_df, name = c,
                   style_function = lambda feature: {
                   "fillColor": colormap4(feature["properties"][c]),
                   "color" : "black", "weight" : 1, "fillOpacity" : 0.4}).add_to(m)

m.add_child(folium.LayerControl())
m.save("ca_folium.html")


m.add_child(folium.LayerControl(collapsed = False))
m.save("ca_folium.html")
