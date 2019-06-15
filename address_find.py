"""
Version: 0.1
Author: lvtoo
e-mail: o@oouul.com
Date: 2019/6/14

"""
import requests
from bs4 import BeautifulSoup


def get_address(t):
    f = open('data/adress'+str(t), 'w')
    for page in range(1, 6):
        a_url = "http://www.win4000.com/meinvtag" + str(t) + "_" + str(page) + ".html"
        r = requests.get(a_url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'lxml')
        div = soup.find('div', class_='w1180 clearfix')
        ul = div.find('ul', class_='clearfix')
        a = ul.find_all('a')
        for i in a:
            f.write(i["href"])
            f.write('\n')


def main():
    # beauty_type 2 美女 3 清纯 4性感 5明星 6空姐校园制服 7游戏  26 cosplay
    beauty_types = [2, 3, 4, 5, 6, 7, 26]
    for beauty_type in beauty_types:
        get_address(beauty_type)


if __name__ == '__main__':
    main()
