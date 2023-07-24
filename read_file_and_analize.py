import requests
import os
import random
import time
import sys
import re
import numpy

def method_A():  #  按字词数量来分析
    with open("get_from_web.txt", encoding = 'utf-8') as file:
        all_data = file.readlines()

    all_char_index_counter = numpy.zeros((16**4,))
    times = 0
    for data in all_data:
            times+= 1
            split_trigger = ['\n\n', '\n', '。', '：', '，', '；', '“', '”', '‘', '‘', '《', '》', '——', '？', '！', "、"]
            web_text_marked = data
            for e in split_trigger:
                web_text_marked = web_text_marked.replace(e, "/")

            web_text_splited = web_text_marked.split("/")
            for eachpart in web_text_splited:
                parted = list(eachpart)
                for charactor in parted:
                    if u'\u4e00' <= charactor <= u'\u9fff':
                        unicode_index = int(charactor.encode('unicode-escape').decode().replace("\\u", ""), 16)
                        all_char_index_counter[unicode_index] = all_char_index_counter[unicode_index] + 1

    all_char_and_number = numpy.empty(shape = (16**4, 2), dtype = "object")
    all_char_and_number[:, 1] = all_char_index_counter
    all_char_and_number[:, 0] = range(16**4)

    index = numpy.argsort(-all_char_and_number[:, 1])
    all_chars_amount = all_char_index_counter.sum()
    c = 0
    print('')
    for i in index:

        unicode = hex(i)[2:]
        unicode = '0'*(4 - len(unicode)) + unicode
        unicode = "\\u" + unicode 
        char = bytes(unicode.encode()).decode("unicode_escape")
        '''
        if all_char_and_number[i, 1] != 0:
            c += 1
            print("|", char, "\t", int(all_char_and_number[i, 1]), "\t",  round(100*all_char_and_number[i, 1] / all_chars_amount, 8), "%\t", end = '')

            if c % 5 == 0:
                print("")
        '''

def method_B():  #  按字出现在几篇文中来分析（普遍性分析
    with open("get_from_web.txt", encoding = 'utf-8') as file:
        all_data = file.readlines()

    all_char_index_counter = numpy.zeros((16**4,))
    times = 0
    for data in all_data:
            char_blacklist = []  #  识别过的词储存进来
            times+= 1
            split_trigger = ['\n\n', '\n', '。', '：', '，', '；', '“', '”', '‘', '‘', '《', '》', '——', '？', '！', "、"]
            web_text_marked = data
            for e in split_trigger:
                web_text_marked = web_text_marked.replace(e, "/")

            web_text_splited = web_text_marked.split("/")
            for eachpart in web_text_splited:
                parted = list(eachpart)
                for charactor in parted:
                    if u'\u4e00' <= charactor <= u'\u9fff' and not charactor in char_blacklist:
                        unicode_index = int(charactor.encode('unicode-escape').decode().replace("\\u", ""), 16)
                        all_char_index_counter[unicode_index] = all_char_index_counter[unicode_index] + 1
                        char_blacklist.append(charactor)

    all_char_and_number = numpy.empty(shape = (16**4, 2), dtype = "object")
    all_char_and_number[:, 1] = all_char_index_counter
    all_char_and_number[:, 0] = range(16**4)

    index = numpy.argsort(-all_char_and_number[:, 1])
    all_chars_amount = len(all_data)
    c = 0
    print('')
    for i in index:

        unicode = hex(i)[2:]
        unicode = '0'*(4 - len(unicode)) + unicode
        unicode = "\\u" + unicode 
        char = bytes(unicode.encode()).decode("unicode_escape")
        
        '''
        if all_char_and_number[i, 1] != 0:
            c += 1
            print("|", char, "\t", int(all_char_and_number[i, 1]), "\t",  round(100*all_char_and_number[i, 1] / all_chars_amount, 3), "%\t", end = '')

            if c % 5 == 0:
                print("")
        '''
    return all_char_and_number, all_chars_amount

if __name__ == "__main__":
    method_B()