#!/usr/bin/env python
import time

import requests

def get_urls(file='data/file.txt'):
    data = []
    with open(file, 'r', encoding='utf8') as f:
        for line in f.readlines():
            r = requests.get(line.strip()+"/favicon.ico")
            # print(line)

if __name__ == '__main__':
    get_urls()