from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os


class mzitu():
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
    def get_page_num(self,path, url_admin):
        html = requests.get(url_admin, headers=self.headers)
        soup = BeautifulSoup(html.text, 'lxml')
        nums = soup.find('span', class_='current-comment-page')
        nums =nums.text.strip('[]')
        nums = int(nums)
        # print(nums)
        for num in range(1, nums):
            url = url_admin+'page-'+str(num)+'#comments'
            print(url)
            self.get_pic_url(path,url)

    def get_pic_url(self,path, url):
        browser = webdriver.PhantomJS()
        browser.get(url)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        imgs = soup.select('div > div > div.text > p > img')
        self.mkdir(path)
        for img_url in imgs:
            img_url = img_url.get('src')
            print('图片保存中： ', img_url)
            self.save(path,img_url)





    def save(self,path,img_url):  ##这个函数保存图片

        name = img_url[-36:-4]
        img = self.request(img_url)
        f = open(path+name + img_url[-4:], 'ab')
        print(path+name + img_url[-4:])
        f.write(img.content)
        f.close()

    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("c:\mzitu", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("D:\mzitu", path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False



    def request(self, url):  ##这个函数获取网页的response 然后返回
        content = requests.get(url, headers=self.headers)
        return content

Mzitu = mzitu()
Mzitu.get_page_num('c:\mzitu\\','http://jandan.net/ooxx/')
