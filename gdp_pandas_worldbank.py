import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

gdp = pd.read_csv('GDP_Eastern_Europe.csv')

#we take only data, not additional informations
gdp = gdp[0:-5]
#delete empty column
del gdp['2016 [YR2016]']
#replace '..' string with nan values
gdp.replace('..', np.nan, inplace=True)

# some of the colums are objects, we have to convert to floats, 
#then pivot_table will take them into consideration
#col_list = ['1990 [YR1990]','1991 [YR1991]','1992 [YR1992]','1993 [YR1993]','1994 [YR1994]','1995 [YR1995]']
col_list = gdp.columns[4:].values
gdp[col_list]=gdp[col_list].apply(pd.to_numeric)

#reindex all table, create pivot view
pv2 = pd.pivot_table(gdp,index=['Series Name','Country Code'], dropna=False, fill_value=0.0)
# set the years
pv2.columns= np.arange(1990,2016)


# Get only GPD
pv2.loc['GDP (current US$)'].T
# Get only GPD for Poland
pv2.loc['GDP (current US$)', 'POL']


import seaborn as sns
palette = sns.color_palette("Paired", 10)
#palette = sns.color_palette("colorblind", 10)
sns.set_palette(palette)

pv2.loc['GDP (current US$)'].T.plot(alpha=0.75, rot=45, title="GDP (current US$)")
pv2.loc['GDP per capita (current US$)'].T.plot(alpha=0.75, rot=45, title="GDP per capita (current US$)")
pv2.loc['GDP growth (annual %)'].T.plot(alpha=0.75, rot=45, title="GDP growth (annual %)")
pv2.loc['GDP per capita growth (annual %)'].T.plot(title="GDP per capita growth (annual %)")



#Create regression plots in seaborn

plot_data = pv2.loc['GDP (current US$)'].T.reset_index()
plot_data.rename(columns={'index':'Years'}, inplace=True)
# unpivot the data, change from table view, where we have columns for each 
# country, to big long time series data, [year, country code, value]
melt_data = pd.melt(plot_data, id_vars=['Years'],var_name='Country')
melt_data.rename(columns={'value':'GDP'}, inplace=True)
sns.lmplot(x="Years", y="GDP", hue="Country", data=melt_data, palette="Set1");
sns.plt.title('Regression lines for  GDP (current US$)')


# plot data without western Europe countries
plot_data_without_west = plot_data.copy()
del plot_data_without_west['DEU']    
del plot_data_without_west['FRA']    
del plot_data_without_west['GBR']    
melt_data_without_west = pd.melt(plot_data_without_west, id_vars=['Years'],var_name='Country')
melt_data_without_west.rename(columns={'value':'GDP'}, inplace=True)


sns.lmplot(x="Years", y="GDP", hue="Country", data=melt_data_without_west, palette="Set1");
sns.plt.title('Regression lines for  GDP (current US$)')



# draw bar plot for 4 countries
#transpose data
pv2T = pv2.T
f, ax = plt.subplots(figsize=(14, 8))

# colors from: http://xkcd.com/color/rgb/
sns.barplot(x='Years',y='DEU', data=plot_data,label="DEU", color=sns.xkcd_rgb["lime"])
sns.barplot(x='Years',y='POL', data=plot_data,label="POL", color=sns.xkcd_rgb["cyan"])
sns.barplot(x='Years',y='CZE', data=plot_data,label="CZE", color=sns.xkcd_rgb["blue"])
#sns.barplot(x='Years',y='EST', data=plot_data,label="EST", color=sns.xkcd_rgb["lavender"])
sns.barplot(x='Years',y='HUN', data=plot_data,label="HUN", color=sns.xkcd_rgb["burnt orange"])
#sns.barplot(x='Years',y='SVK', data=plot_data,label="SVK", color=sns.xkcd_rgb["peach"])
#sns.barplot(x='Years',y='UKR', data=plot_data,label="UKR", color=sns.xkcd_rgb["mustard"])

# Add a legend and informative axis label
ax.legend(ncol=2, loc="upper left", frameon=True)
ax.set(xlim=(0, 24), ylabel="",xlabel="gdp")
plt.xticks(rotation=90)
sns.despine(left=True, bottom=True)
plt.show()

