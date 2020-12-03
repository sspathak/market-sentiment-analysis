import requests
from bs4 import BeautifulSoup
import re, datetime
    
def getText(u):
    z=""
    html_text1 = requests.get(u).text
    soup1 = BeautifulSoup(html_text1, 'html.parser')
    article= soup1.find(id="js-article__body")
    if article==None: return('  ')
    for x in article.find_all('a'): x.string=""
    for x in article.find_all('p'):
        z=z+(x.get_text())
        z= z.replace('\r', '').replace('\n', '')
        while '  ' in z:
            z = z.replace('  ', ' ')
    return(z)

f=open("urls")
urls=[]
dates=[]
for u in f:
    u= u.replace('\r', '').replace('\n', '')
    urls.append(u)
    match = re.search('\d{4}-\d{2}-\d{2}', u)
    date = match.group()
    dates.append(date)

dates, urls =  (list(t) for t in zip(*sorted(zip(dates, urls))))

prev=1
for i in range(1,len(dates)):
    if dates[i]==dates[i-1]:
        dates[i-1]=dates[i-1]+","+str(prev)
        prev=prev+1
    else:
        dates[i-1]=dates[i-1]+","+str(prev)
        prev=1


for i in range(len(urls)):
    url=urls[i]
    print url
    t=getText(url)
    out = open(dates[i], "w")
    out.write(t.encode("utf-8"))

