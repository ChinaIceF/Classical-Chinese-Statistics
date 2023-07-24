import requests
import os
import random
import time
import sys

def clear_html(text):
    text = text.replace('	', '')
    text = text.replace('<span class="pinyin">', '\n')
    text = text.replace('</span>', ' ')
    text = text.replace('<span class="fontred">', ' ')
    text = text.replace('<br />', '\n')
    text = text.replace('</div>', '')

    return text

def getwebdata(URL):
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
                ]
    headers = {'User-Agent': random.choice(user_agent_list)}    
    res = requests.get(URL, headers = headers)
    res.encoding = 'UTF-8'
    textURL = res.text
    return textURL


def _api_get_char_translate(char):
    URL = 'https://wyw.hwxnet.com/view.do?keyword=' + char
    text = getwebdata(URL)
    
    useful_text = clear_html(text.split('\n')[96])
    return useful_text