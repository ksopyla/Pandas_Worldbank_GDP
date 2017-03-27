# Pandas+Seaborn tutorial on World bank GDP data for central and eastern Europe


Project analysys the gross domestic product (GDP) data for 10 central and eastern European countries.
The analysis was prepared based on the World Bandk Data, particulary the dataset [World Development Indicatiors](http://databank.worldbank.org/data/reports.aspx?source=world-development-indicators)
was utilized. This set contains many different economic development indicators you can choose from. 
For simplicity I focused on four of them: GDP per capita ( US$), GDO per capita growth (annual %), GDP growth (annual %),  GDP (current US$).


Data cleaning, manipulation and data transformation was done with with use of [Pandas](http://pandas.pydata.org/) - 
easy-to-use data structures and data analysis tools for python. Additionaly there are many visusalization, where some of them were
prepared with matplotlib but [regression plots](http://seaborn.pydata.org/generated/seaborn.lmplot.html) and 
[bar plots](http://seaborn.pydata.org/generated/seaborn.barplot.html) were created with [seaborn](http://seaborn.pydata.org/) library. 

This project will introduce the basic Pandas concept like: 
[data frames](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html), 
[data transformations with apply function](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html), 
[reshaping and pivot tables](http://pandas.pydata.org/pandas-docs/stable/reshaping.html) etc.

I choose pandas and seabor because you can easily pass pandas data frame to seaborn and 
plot data from interesting columns or rows. 

Sample plots:

![GDP per capita (current US$)](https://plon.io/files/58bab9581b12ce00012bd610)
![Regression plots for GDP](https://plon.io/files/58babdee1b12ce00012bd63a)

This short youtube video presents what type of visualization is generated:

[![World Bank Pandas Plot](https://img.youtube.com/vi/G1-HSWJmvEw/0.jpg)](https://www.youtube.com/watch?v=G1-HSWJmvEw)



## Project description 

In order to be practical and choose interesting subject. I challange myself and try to answer
the question: 
**How far in economic development eastern Europe countries are relative to developed 
countries like Germany and France?**

This led to analyzing four GDP factors:

* GDP per capita ( US$)
* GDO per capita growth (annual %)
* GDP growth (annual %)
* GDP (current US$)


For further analysis, the 10 countries were choosen:
* Poland
* Germany
* Belarus
* Czech Republic
* Slovak Republic
* Hungary
* Estonia
* France
* UK
* Ukraine

## What will you learn? 

This project is compose in such a way to teach you data analysis pipline. You will start
with reading csv file, clean the data, transform data to more appropriete structure and finaly
visualize interesting columns or rows from data frame.


You will learn: 

* How to read cvs files into Pandas Data Frame
* How to clean the data, remove missing values, remove unnecessary columns, convert dates etc.
* How to create pivot table in Pandas
* How to create plots based on pandas data frame
* How to create regression plots in seaborn (sns.lmplot)
* How to create bar plot witch stacked collumns



## Project structure

The project contains two file, first contains raw csv data taken from World Bank website. The second file
is python script with all the pandas and seaborn code:  

* GDP\_Eastern\_Europe.csv - data file, generated from World Bank Development Indicators
* gdp\_pandas\_woldbank.py - main file with analysis and plots




## Grab the code or run project in online IDE

* You can [download code from github](https://github.com/ksopyla/Pandas_Wordbank_GDP)
* You can [run the project in your browser](https://plon.io/explore/wordbank-gdp-analysis/o3IJwRgA3H4e2QtyZ)
