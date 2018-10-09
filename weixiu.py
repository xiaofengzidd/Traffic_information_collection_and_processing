from pyquery import PyQuery as pq
from selenium import webdriver
# from bs4 import BeautifulSoup
import requests
import codecs
# import time
import re

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
a = webdriver.Chrome(chrome_options=chrome_options)

def shouji_list():
    a.get('https://www.hiweixiu.com/step/selectInfo')
    html = a.page_source
    doc = pq(html)
    htm = doc('.telephone_list').html()
    patt = re.compile(r'href="(.*?)">', re.S)
    urlss = re.findall(patt,htm)
    return urlss

if __name__ == '__main__':
    url_name = shouji_list()
    print(url_name)
    with codecs.open(r'C:\Users\Liu\Desktop\apple_repair.txt', 'a', encoding='utf-8') as f:
        for num in url_name:
            try:
                # id_list = list()
                price_url = 'https://www.hiweixiu.com'+str(num)
                response = requests.get(price_url)
                patt = re.compile(r'class="rp_info"(.*?)class="rp_id"',re.S)
                id_html = re.findall(patt,response.text)
                patte = re.compile(r'"rp_id":"(.*?)".*?"faulttype_id":"(.*?)"',re.S)
                ids = re.findall(patte,id_html[0])
                for id in ids:
                    rid, fid = id
                    zz_url = 'https://www.hiweixiu.com/step/info?plan=%s&fid=%s'%(rid, fid)
                    a.get(zz_url)
                    html = a.page_source
                    patt = re.compile(r'userinfoR">(.*?)userinfoPrice">', re.S)
                    resus = re.findall(patt, html)
                    pat = re.compile(r'</span>(.*?)</li>.*?</span>(.*?)</li>.*?</span>(.*?)</li>.*?</span>(.*?)</li>.*?</span>(.*?)</li>.*?</span>(.*?)</li>',re.S)
                    resuls = re.findall(pat, resus[0])
                    for resul in resuls:
                        pro, bra, title, fail, repa, price = resul
                        print(pro + ' ' + bra + ' ' + title + ' ' + fail + ' ' + repa + ' ' + price)
                        f.write(pro + ':' + bra + ':' + title + ':' + fail + ':' + repa + ':' + price+'\r\n')
            except:
                print('error')