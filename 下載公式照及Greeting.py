from bs4 import BeautifulSoup as bs
import requests
import urllib.request
import os
import io
import sys
import warnings
import json
warnings.filterwarnings("ignore")


def get_html(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def downloadImg(memName, srcLink, savedir):
    if not os.path.isdir(savedir):
        os.makedirs(savedir)
    tmp = requests.get(srcLink)
    with open(savedir + "/" + memName +'.jpg', 'wb') as f:
                f.write(tmp.content)
    return "OK"


memList = ["2", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]

for memNum in memList:
    url = "https://www.hinatazaka46.com/s/official/artist/" + str(memNum) + "?ima=0000"
    html = get_html(url)
    res = bs(html)
    memPic = res.find(class_="c-member__thumb c-member__thumb__large").find('img')['src']
    memName = res.find(class_="c-member__name--info").text.strip()
    memCard = res.find(class_="c-member-greeting-item-card").find('img')['src']
    downloadImg(memName, memPic, "Pic")
    downloadImg(memName, memCard, "Greeting")
    print(memName)
