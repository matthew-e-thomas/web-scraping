#Some analysis from csv file I obtained from scraping Totalwine.com. See totalwinelist.py for scrapy code

import pandas as pd
import matplotlib.pyplot as plt #Using pandas for dataframe, matplotlib for visualization

df = pd.read_csv('/Users/matthewthomas/totalwine/totalwine/totalwinelist.csv', sep=",", header=0)#read csv doc we made in scrapy

#we can run a few commands to find out things about the list that may be of interest

#For example, what if we want to know what the maximum price is and which wine is the most expensive?
max_price = df['Price'].max()
print(max_price)

most_expensive_wine = df[df['Price'] == max_price]['Product']
print(most_expensive_wine)

#Where is the most expensive Pinot from?
expensive_desc = df.loc[84, 'Description']
print(expensive_desc)
#Looks like it's from Italy

#What about average price?
avg = df["Price"].mean()
print(avg)

#What if we want to see which wines are from the Willamette Valley in Oregon?
oregon = df['Description'].str.contains("Willamette")
#let's see all the wines from this region
df.Product[oregon]

#Let's do a quick visualization to see what kind of prices these wines fetch
df[oregon].plot("Product","Price", kind='bar')
#Looks like most are between $10 and $20 but one is about $50

#What is we want to know which wines contain a certain descriptor?
tobacco = df['Description'].str.contains("tobacco")
df[tobacco]

#we can find a couple of other subgroups of certain regions and compare them
sonoma = df['Description'].str.contains("Sonoma")
burgundy = df['Description'].str.contains("Burgundy")

df[sonoma].describe()
df[burgundy].describe()
#Looks like Sonoma Pinots that are popular cost a bit more

df[sonoma].plot("Product","Price", kind='box')
#We can visualize the distribution and see the average sonoma Pinot is just under $20
