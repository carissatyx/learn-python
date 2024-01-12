# Step 1: fake_useragent to call urls
# Step 2: BeautifulSoup to scrape content
# Step 3: Use collections to count keywords 

#%% 
import requests
import json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import io
import time
import pandas as pd
from collections import Counter

address =['https://www.coingecko.com/en/coins/bitcoin']
ua = UserAgent()
headers = {'User-Agent': ua.chrome}

def gkbAPI(keyword): 
    url = "https://kgsearch.googleapis.com/v1/entities:search?query="+keyword+"&key=&limit=1&indent=True" #rmb to add you API keys

    payload = {}
    headers = {}

    response = requests.request("GET",url,headers=headers,data=payload)

    data = json.loads(response.text)

    try: 
        getlabel = data['itemListElements'][0]['result']['@type']
    except: 
        getlabel = ['none']
    return getlabel

fulllist = []
for row in address: 
    time.sleep(1)
    url = row
    print(url)

    res = requests.get(url,headers=headers)
    html_page = res.content

soup = BeautifulSoup(html_page,"html.parser")
text = soup.find_all(text = True)

stopwords = ['get','ourselves', 'hers','us','there','you','for','that','as','between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'style',
    'input'
]

ban_chars = ['|','/','&']

for t in text: 
    if t.parent.name not in blacklist: 
        output += t.replace("\n","").replace("\t","")
output = output.split(" ")

output = [x for x in output if not x=='' and not x[0] =='#' and x not in ban_chars]
output = [x.lower() for x in output] 
output = [word for word in output if word not in stopwords]

fulllist += output

counts = Counter(output).most_common(10)

for key, value in counts: 
    getlabels = gkbAPI(key)
    strgetlabels = ','.join(getlabels)
    readout = str(key) + ": {:>0}" + " | Entity Labels: "+ strgetlabels
    print(readout.format(str(value)))
print("\n")
# %%
