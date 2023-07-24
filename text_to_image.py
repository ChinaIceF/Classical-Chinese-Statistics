
#载入必要的模块
import pygame
import random
import numpy
import time
import read_file_and_analize

all_char_and_number, articles_amount = read_file_and_analize.method_B()

def get_random_color():
    return (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255))

def get_color(char):
    _largest_color = numpy.array([255, 255, 255])
    _mid_color = numpy.array([255, 255, 255])
    _smallest_color = numpy.array([120, 120, 255])
    
    _mid_threshold = 0.35
    
    unicode_index = int(char.encode('unicode-escape').decode().replace("\\u", ""), 16)
    frequenty = all_char_and_number[unicode_index, 1] / articles_amount

    if frequenty < _mid_threshold:
        t = (_mid_threshold - frequenty) / _mid_threshold
        color = _smallest_color * t + _mid_color * (1-t)
    else:
        t = (frequenty - _mid_threshold) / (1 - _mid_threshold)
        color = _largest_color * t + _mid_color * (1-t)

    return color

def text_to_image(text):
    #  处理 text
    _max_x_chars = 40       #  每行最多字符数
    _char_size = 32
    _x_bias = 100
    _y_bias = 100
    _x_space = 32
    _y_space = 64
    
    pic_size = (2*_x_bias + _x_space * (_max_x_chars - 1), 2*_y_bias + _y_space * int(len(text)/_max_x_chars))
    
    pygame.init()
    pic = pygame.Surface(pic_size)
    pic.fill((255,255,255))
    font = pygame.font.SysFont('Microsoft YaHei', _char_size)
    for i in range(len(text)):
        char = text[i]
        if u'\u4e00' <= char <= u'\u9fff':
            color = get_color(char)
        else:
            color = (255,255,255)

        single_char = font.render(char, True, (0, 0, 0), color)
        pic.blit(single_char,[_x_bias + (i%_max_x_chars)*_x_space, _y_space + (i//_max_x_chars)*_y_space])

    filename = time.asctime(time.localtime(time.time())).replace(":", "-")
    pygame.image.save(pic, "./temp/{}.png".format(filename))#图片保存地址
    return filename

def generate_image(text):
    return text_to_image(text)
