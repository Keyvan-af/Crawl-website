#Libraries requirments
'''
!pip install requests
!pip install html5lib
!pip install bs4
!pip install fake_useragent
'''

#Python program to scrape website
#and save news from website

#import packages
import pandas as pd
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import csv
import time
from tqdm.notebook import trange, tqdm
from fake_useragent import UserAgent
from retrying import retry
import glob
ua = UserAgent()
header = {
    "User-Agent": ua.random
}

# create empty arrays
summery = []
url = []
title = []

# Define a retry strategy
@retry(stop_max_attempt_number=4, wait_fixed=2500)
def make_request(page):
        try:
          r = requests.get(page, headers=header, timeout=(4))
        except requests.exceptions.Timeout:
          print("request timeout error on Page")    
          pass
        soup = BeautifulSoup(r.content, 'html5lib')
        table = soup.find('section', attrs = {'class':"content"})
        #Extract urls from website
        for i in table.findAll("article",{"class":"list-item"}):
            summery.append(i.h4.text)
            url.append(i.a['href'])
            title.append(i.img['alt'])
        #Use time sleep to dont get error from website
        time.sleep(4)
        return url

#Need root of the urls to attach with url that we extract from website
root_u = 'https://www.tasnimnews.com'

# create empty arrays
urls = []
News_article=[]

# Define a retry strategy
@retry(stop_max_attempt_number=4, wait_fixed=2500)
def get_url(sub_u):
    #request to pages, pull htmls and read with  BeautifulSoup
    try:  
      re = requests.get(root_u + sub_u, headers=header, timeout=(4))    
    except requests.exceptions.Timeout:
        print('request timeout error on text page')
        pass
    #Appending gets requested to urls
    if re.status_code == 200:
          urls.append(re)
    #Use time sleep to dont get error from website
    time.sleep(4)
    return urls

# store root url without page number
root = 'https://www.tasnimnews.com/fa/service/3/%D9%88%D8%B1%D8%B2%D8%B4%DB%8C'

# create empty arrays
soups = []
tables = []

for p in trange(1,3):
    # create empty arrays
    url = []
    urls = []
    soups = []
    try:
        ur = make_request(root + "?page="+str(p))
        for u in trange(len(ur)):
            get_url(ur[u])
        #Convert htmls to BeautifulSoups
        for u in range(len(urls)):
            s = BeautifulSoup(urls[u].content, 'html5lib')
            soups.append(s)  
        #Find tables in BeautifulSoups
        for s in range(len(soups)):
            t = soups[s].find('div', attrs = {'class':"story"})
            tables.append(t)
        #Find news in tables    
        for t in range(len(tables)) :  
            News_article = []
            news = []  
            for k in tables[t].findAll("p", {"style":"text-align:justify"}):
                News_article.append(k.text)    
            news ="".join(News_article)
            pa = Path(f'Data/{p}').mkdir(parents=True, exist_ok=True)
            with open(Path.cwd() /'Data'/f'{p}'/f'{t+1}.txt', 'a') as f:
                    f.write(news)
    except:
        print("error")
        pass

#using glob to extract text
all_news = []
for name in glob.iglob('***/**/*.txt'):
    with open(name, 'rt') as fd:
        t=fd.read()
        all_news.append(t)
        
#save to csv
df = pd.DataFrame({'title': title,
                   'summery': summery,
                   'all_news': all_news})
df.to_csv('New.csv', index=False, encoding='utf-8-sig')