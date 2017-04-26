# -*- coding: utf-8 -*-
import codecs
import requests
import re
from bs4 import BeautifulSoup

f = codecs.open('dy_crawler.txt', 'a', 'utf-8')

for p_num in range(1, 180):
    url = "http://program.tving.com/tvn/dokebi/4/Board/List?page={}".format(p_num)
    res = requests.get(url)
    soup = BeautifulSoup(res.content)

    for x in soup.find_all('td', attrs={'class': 'title'}):
        urls = "http://program.tving.com/" + x.a['href']
        res2 = requests.get(urls)
        soup2 = BeautifulSoup(res2.content)

        if urls[-4:] == '2491' or urls[-4:] == '2300' or urls[-4:] == '2081':
            pass
        else:
            for contents in soup2.find_all('div', attrs={'class': 'ContentWrap'}):
                title = contents.p.get_text()
                content = re.sub(r'\s+', ' ', contents.select('div.area_con')[0].get_text())
                date = contents.select('span.date')[0].get_text()[5:10]
                view = contents.select('span.view')[0].get_text()
                f.write(date+'\t'+view+'\t'+title+'\t'+content+'\n')
                print title

f.close()
