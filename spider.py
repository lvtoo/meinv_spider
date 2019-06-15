"""
Version: 0.1
Author: lvtoo
e-mail: o@oouul.com
Date: 2019/6/14

"""
import requests
from bs4 import BeautifulSoup
from multiprocessing import Process


def get_type(beauty_type):
    # beauty_type 2 美女 3 清纯 4性感 5明星 6空姐校园制服 7游戏  26 cosplay
    file = {2: "beauty",
            3: "young",
            4: "sexy",
            5: "star",
            6: "campus",
            7: "game",
            26: "cosplay",
            }
    return file[beauty_type]


def type_work(beauty_type):
    f = open('data/adress' + str(beauty_type), 'r')
    urls = f.readlines()
    for u in urls:
        u = u[:-1]
        r = requests.get(u)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'lxml')
        a = int(soup.find('div', class_='ptitle').em.get_text())
        for i in range(1, a + 1):
            url = u[:-5] + '_' + str(i) + u[-5:]
            r = requests.get(url)
            r.encoding = 'utf-8'
            soup = BeautifulSoup(r.text, 'lxml')
            img = soup.find('img', class_='pic-large')
            div = soup.find('div', class_='ptitle')
            title = div.get_text().replace('/', '-').replace(' ', '')

            with open('M:/img/' + get_type(beauty_type) + '/' + str(title) + ".jpg", 'wb') as f:
                f.write(requests.get(img['url']).content)
                f.close()


def main():
    beauty_types = [2, 3, 4, 5, 6, 7, 26]

    for beauty_type in beauty_types:
        Process(target=type_work, args=(beauty_type,)).start()


if __name__ == '__main__':
    main()
