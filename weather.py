#importing packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

#chose the weather.com news page 
page = requests.get('https://weather.com/news')
page

#create BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
soup

print(soup.prettify())

#find title of news articles 
titles = soup.find_all('div', class_='CollectionMediaList--title--2ELr1')
list_titles = []
for i in titles:
    print(i.text)
    data = i.text
    list_titles.append(data)
list_titles

#compare to see if it matches number on site 
len(list_titles)

#get caption of news articles 
captions = soup.find_all('div', class_='CollectionMediaList--caption--3Md1w')
list_captions = []
for i in captions:
    print(i.text)
    data = i.text
    list_captions.append(data)
list_captions

#create dataframe from information 
df = pd.DataFrame({'Title of Article':list_titles,'Caption':list_captions})
df

#put data into csv file
df.to_csv('./data/weather_news_articles.csv')