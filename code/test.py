import requests
from bs4 import BeautifulSoup

l=[]


baseURL='https://www.marketwatch.com/search?q=TSLA&m=Ticker&rpp=100&mp=0&bd=true&bd=false&bdv=03%2F31%2F2020&rs=true'
urls=[baseURL]
for i in range(1,13):
    urls.append(baseURL+'&o='+str(i*100+1))
print urls


for u in urls:
    html_text1 = requests.get(u).text
    soup = BeautifulSoup(html_text1, 'html.parser')
    for link in soup.find_all('a'):
        x=link.get('href')
        if x.find('story')>=0 and x.find('http')>=0: l.append(x)


for x in l: print x    
