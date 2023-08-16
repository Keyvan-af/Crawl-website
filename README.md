# Crawl-website
[![Follow](https://img.shields.io/twitter/follow/gensim_py.svg?style=social&style=flat&logo=twitter&label=Follow&color=blue)](https://twitter.com/KAfzalnia76689)

Crawling tasnim website and EDA
## Web scraping
[script.py](https://github.com/Keyvan-af/Crawl-website/blob/main/script.py) is my code that scrapping on [tasnim website](https://www.tasnimnews.com/fa/service/3/%D9%88%D8%B1%D8%B2%D8%B4%DB%8C), sport section using bs4
### Installation
```bash
pip install requests
pip install html5lib
pip install bs4
pip install fake_useragent
```
### Description
- function to request each page of the website and extract title, summary and URL
- we want the news text, so we get the URLs and each URL address takes us to a page from which we can extract the news text.
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
sub_u is the url we extract with the make_request function

- We use pathlib to store txt files in a directory and glob to append all news.
- And at the end of the code, the data is stored in a csv file.
## EDA
As we know Exploratory Data Analysis (EDA) is the process by which the data analyst becomes acquainted with their data to drive intuition and begin to formulate testable hypotheses.

#### Note:
Farsi texts in plotting do not have a good view. They are reversed, so I use arabic_reshaper package and import reshape to show properly.
##### Example usage in [notebook](https://github.com/Keyvan-af/Crawl-website/blob/main/EDA.ipynb)
```python
x1=[get_display(reshape(label)) for label in x]
```
