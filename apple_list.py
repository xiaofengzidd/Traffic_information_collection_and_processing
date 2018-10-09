
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import codecs
# import time
# import re
#
def shouji_list():
    phonename = dict()
    for i in range(1,2):#采集1到2页的手机价格
        url = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exprice_M2800L4499%40exbrand_14026&page='+str(i)+'&stock=1&sort=sort_rank_asc&trans=1&JL=4_7_0#J_main'
        url_session = requests.Session()
        #会话对象requests.Session能够跨请求地保持某些参数，比如cookies，即在同一个Session实例发出的所有请求都保持同一个cookies,而requests模块每次会自动处理cookies
        #这样就很方便地处理登录时的cookies问题。在cookies的处理上会话对象一句话可以顶过好几句urllib模块下的操作。
        req = url_session.get(url).text
        soup = BeautifulSoup(req, 'html.parser')
        phone_html = soup.find_all(name = 'div', attrs = {'class':"p-name"})#查看网页源代码得到的关键信息
        for item in phone_html:
            for link in item.find_all('a'):
                shouji_html = str(link.get('href')[14:-5])#取得每个手机网址的关键信息
                phonename[shouji_html] = link.get_text().strip()#将价格和网址对应，组成一个字典
    return phonename

if __name__ == '__main__':
    price = shouji_list()
    with codecs.open(r'C:\Users\Liu\Desktop\apple.txt', 'a', encoding='utf-8') as f:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        a = webdriver.Chrome(chrome_options=chrome_options)
        # a = webdriver.Chrome()
        for num in price:
            try:
                xz = list()
                price_url = 'http://item.jd.com/'+str(num)+'.html'
                url_session = requests.Session()
                req = url_session.get(price_url).text
                soup = BeautifulSoup(req, 'html.parser')
                phone_html = soup.find_all(name='div', attrs={'class': "p-choose"})
                for item in phone_html:
                    for link in item.find_all(name='div', attrs={'class': "item"}):
                        xz_html = str(link.get('data-sku'))
                        xz.append(xz_html)
                # print(xz)

                for i in range(1,len(xz)+1):
                    price_xz = 'https://item.jd.com/'+str(xz[i])+'.html'
                    # print(price_xz)
                    # f.write(price_xz+'\r\n')
                    a.get(price_xz)
                    b = a.find_element_by_class_name('summary-price')
                    pri = b.find_element_by_class_name('p-price')
                    tit = a.find_element_by_class_name('sku-name')
                    print(str(tit.text) + ':' + str(pri.text)+price_xz + '\n')
                    f.write(str(tit.text) + ':' + str(pri.text)+price_xz + '\r\n')
            except:
                # print('None')
                # f.write('None'+'\r\n')
                print(str(tit.text) + ':' + 'None'+price_xz + '\n')
                f.write(str(tit.text) + ':' + 'None'+price_xz + '\r\n')
