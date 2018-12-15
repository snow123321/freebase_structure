#encoding=utf-8

from bs4 import BeautifulSoup
import urllib.request
from pandas import Series
from selenium import webdriver
from time import sleep




url="http://en.wikipedia.org/wiki/Kevin_Bacon"
#使用Chrome浏览器
driver = webdriver.Chrome(executable_path='./driver/chromedriver')
#使用Firefox浏览器
#driver=webdriver.Firefox()
driver.get(url)
html=driver.page_source

#headers={'User-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
#data1=urllib.request.Request(url,headers=headers)
#html=urllib.request.urlopen(data1)

html=urllib.request.urlopen(url)
soup=BeautifulSoup(html,"lxml")

a_all=soup.find_all("a")
for link in a_all:
    if "href" in link.attrs:
        print(link.attrs["href"])