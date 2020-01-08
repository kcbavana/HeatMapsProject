# -*- coding: utf-8 -*-
"""
Created on Mon Dec 2 14:54:09 2019

@author: kcbav

Project 6
"""
import geopandas as gpd
import pandas
import matplotlib.pyplot as plt

fileref = open('Crimes.csv', 'r')
df = pandas.read_csv(fileref)
communities = gpd.read_file('Boundaries_Community.geojson')


def com_count(df, col, value, unique_id, com_num):
    """Returns count of unique_id in df com_num rows w/entry value in column col"""
    rows = df[df[col] == value] # boolean slice of rows we want
    if com_num not in rows['Community Area'].values:
        return 0
    grouped = rows.groupby('Community Area')
    return grouped[unique_id].count()[com_num]

def make_dictionary(df, col, value, unique_id):
    """Returns dictonary of the unique Id with every 77 ids"""
    my_dict = {}
    for i in range(1,78):
        my_dict[i]= com_count(df, col, value, unique_id,i)
    #print(my_dict.get(73))
    return my_dict

#make_dictionary(df, "Primary Type", "SEX OFFENSE", "Case Number")
    
#graph 1
sex_offence_graph = make_dictionary(df, "Primary Type", "SEX OFFENSE", "Case Number")
ls = []
for x in range(1,78):
    s = sex_offence_graph.get(x)
    ls.append(s)
communities["SEX OFFENSE"] = ls
fig, ax = plt.subplots() # gives back tuple of figue, axes
ax.set_title("Sex offence in chicago community area")
fig.set_size_inches (10, 10) # Just controls size; try other numbers
communities.plot(column='SEX OFFENSE', scheme='quantiles', edgecolor='black', ax=ax, legend=True)
plt.savefig("Sex Offence heat map")

#graph 2
THEFT_graph = make_dictionary(df, "Primary Type", "THEFT", "Case Number")
ls2 = []
for y in range(1,78):
    t = THEFT_graph.get(y)
    ls2.append(t)
communities["THEFT"] = ls2
fig, ax = plt.subplots() # gives back tuple of figue, axes
ax.set_title("Theft crimes in chicago community area")
fig.set_size_inches (10, 10) # Just controls size; try other numbers
communities.plot(column='THEFT', scheme='quantiles', k=10, edgecolor='black', ax=ax, legend=True)
plt.savefig("Theft Crime heat map")

#graph 3
CRIMINAL_TRESPASS_graph = make_dictionary(df, "Primary Type", "CRIMINAL TRESPASS", "Case Number")
ls3 = []
for z in range(1,78):
    c = CRIMINAL_TRESPASS_graph.get(z)
    ls3.append(c)
communities["CRIMINAL TRESPASS"] = ls3
fig, ax = plt.subplots() # gives back tuple of figue, axes
ax.set_title("Criminal Trespass in chicago community area")
fig.set_size_inches (10, 10) # Just controls size; try other numbers
communities.plot(column='CRIMINAL TRESPASS', cmap='summer',scheme='quantiles', k=15, edgecolor='black', ax=ax, legend=True)
plt.savefig("Criminal Trespass heat map")

