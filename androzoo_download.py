# coding:utf-8

import requests
import urllib.request
import threading
import argparse
#27787e752bcb4d015a9c2fe6fdaf0ef54a628ff16af1f19ef15ffc7fd0664fbc
# import time
base_url = 'https://androzoo.uni.lu/api/download?apikey=your key =%s'

global c
global count


def download(sha256, year, type):
    global c
    global count
    url = base_url % sha256
    # start = time.time()
    r = requests.get(url=url)
    # print("request")
    # end = time.time()
    # print(end-start)
    if r.status_code == 200:
        urllib.request.urlretrieve(url,
                                   '/home/lhd/apk/androzoo/' + year + '/' + type + '/%s.apk' % sha256)
        c += 1
        print("**********下载个数：%d, 下载进度：%f %%**********" % (c, 100 * round(c / 284, 3)))
        print('downloaded', sha256)
    # print("download count:", count)
    count -= 1


if __name__ == "__main__":
    year = '2017'
    type = 'benign'
    count = 0
    c = 0
    with open('/home/lhd/apk/androzoo/sha256/' + year + '_' + type + '.txt',
              'r') as tf:
        for line in tf:
            sha256 = line.rstrip('\n')
            # print(sha256)
            while (count >= 20):
                continue
            # print('count', count)
            count += 1
            t = threading.Thread(target=download, args=(sha256,year,type,))
            t.setDaemon(False)
            t.start()
        if c % 50 == 0:
            print("**********下载个数：%d, 下载进度：%f**********" % (c, c / 20))

    type = 'malware'
    count = 0
    c = 0
    with open('/home/lhd/apk/androzoo/sha256/' + year + '_' + type + '.txt',
              'r') as tf:
        for line in tf:
            sha256 = line.rstrip('\n')
            # print(sha256)
            while (count >= 20):
                continue
            # print('count', count)
            count += 1
            t = threading.Thread(target=download, args=(sha256,year,type,))
            t.setDaemon(False)
            t.start()
        if c % 50 == 0:
            print("**********下载个数：%d, 下载进度：%f**********" % (c, c / 20))

    year = '2018'
    type = 'malware'
    count = 0
    c = 0
    with open('/home/lhd/apk/androzoo/sha256/' + year + '_' + type + '.txt',
              'r') as tf:
        for line in tf:
            sha256 = line.rstrip('\n')
            # print(sha256)
            while (count >= 20):
                continue
            # print('count', count)
            count += 1
            t = threading.Thread(target=download, args=(sha256,year,type,))
            t.setDaemon(False)
            t.start()
        if c % 50 == 0:
            print("**********下载个数：%d, 下载进度：%f**********" % (c, c / 20))

    year = '2019'
    type = 'malware'
    count = 0
    c = 0
    with open('/home/lhd/apk/androzoo/sha256/' + year + '_' + type + '.txt',
              'r') as tf:
        for line in tf:
            sha256 = line.rstrip('\n')
            # print(sha256)
            while (count >= 20):
                continue
            # print('count', count)
            count += 1
            t = threading.Thread(target=download, args=(sha256,year,type,))
            t.setDaemon(False)
            t.start()
        if c % 50 == 0:
            print("**********下载个数：%d, 下载进度：%f**********" % (c, c / 20))
