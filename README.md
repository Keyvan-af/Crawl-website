# Crawl-website
[![Follow](https://img.shields.io/twitter/follow/gensim_py.svg?style=social&style=flat&logo=twitter&label=Follow&color=blue)](https://twitter.com/KAfzalnia76689)

Crawling tasnim website and EDA
## Web scraping
script.py is my code that scrapping on [tasnim website](https://www.tasnimnews.com/fa/service/3/%D9%88%D8%B1%D8%B2%D8%B4%DB%8C), sport section using bs4
### Installation
```bash
pip install requests
pip install html5lib
pip install bs4
pip install fake_useragent
```
### Description
- function for making request to each page of website and extract title, summery and url
- we want news text so we get urls and each url address us to page that we can extract news text.
```python
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
```
sub_u is url that we extract with make_request function

- We use pathlib to saving txt files in dir and using glob to append all news.
- And at the end of the code saving data to csv file.
## EDA
As we know Exploratory Data Analysis (EDA) is the process by which the data analyst becomes acquainted with their data to drive intuition and begin to formulate testable hypotheses.
### Notebook Outline:
- Environment set-up
- Loading Data and get a brief overview of columns
- Preprocessing and EDA
- Conclusions
#### Note:
Farsi texts in plotting don't have good view. They are vice versa so i use arabic_reshaper package and import reshape to show correctly.
##### Example usage in code
```python
x1=[get_display(reshape(label)) for label in x]
```
