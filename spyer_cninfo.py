import os

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import time

url_link = "http://www.cninfo.com.cn/cninfo-new/disclosure/szse"

driver = webdriver.Chrome()
driver.get(url_link)
htmlSource = driver.page_source

print(htmlSource)
# if __name__ == '__main__':
#     list_url = []
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
#     }
#     req = requests.get(url=url_link, headers=headers)
#     req.encoding = 'utf-8'
#     html = req.text
#     bf = BeautifulSoup(html, 'lxml')
#     print(bf.prettify)
#     # targets_url= bf.find_all('ul',id='ul_a_latest')
#     # news_title_link = {}
#     #
#     #
#     # for url in targets_url[0]:
#     #     print (url)
#     #     url_url = BeautifulSoup(str(url), 'lxml')
#     #     news_title_link["code"] = url_url.find_all('div',class='t1').get('code')
#     #     news_title_link["code"] = url_url.find_all('div', class ='t2').font.getText()
#     #
#     # # ul_a_latest