import requests
from bs4 import BeautifulSoup

l=[]

ticker_name = 'TSLA' # name of the ticker
baseURL='https://www.marketwatch.com/search?q=' + ticker_name + '&m=Ticker&rpp=100&mp=0&bd=true&bd=false&bdv=05%2F31%2F2020&rs=true'
# the base url set up to accumulate marketwatch articles under advanced search for the given ticker starting from May 31st (modifiable) going back all the way to 13 pages prior

urls=[baseURL]
for i in range(1,13):
    urls.append(baseURL+'&o='+str(i*100+1))
# store urls in an array


for u in urls:
    html_text1 = requests.get(u).text
    soup = BeautifulSoup(html_text1, 'html.parser')
    for link in soup.find_all('a'):
        x=link.get('href')
        if x.find('story')>=0 and x.find('http')>=0: l.append(x)

    # collectively store the URLs of all the relevant web pages corresponding to the marketwatch articles.

for x in l: print(x)

# run in terminal and write onto a file named urls
