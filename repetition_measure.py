import numpy
import time

def _evaluate_func_A_checking(length, is_same_array, mask_array, s, _y, _x):
    length += 1
    new_y = _y + 1
    new_x = _x + 1
    if new_y < s[0] and new_x < s[1]:
        if is_same_array[new_y][new_x] == 1 and is_same_array[new_y][new_x] == 1:
            length = _evaluate_func_A_checking(length, is_same_array, mask_array, s, new_y, new_x)

    return length


def evaluate_func_A(is_same_array):
    s = is_same_array.shape  # [B, A]
    mask_array = numpy.ones(s)
    length_list = []
    for y in range(s[0]):
        for x in range(s[1]):
            if is_same_array[y][x] == 1 and mask_array[y][x] == 1:
                length = _evaluate_func_A_checking(0, is_same_array, mask_array, s, y, x)
                length_list.append(length)
                mask_array[y:y+length, :] = mask_array[y:y+length, :] * 0
                mask_array[:, x:x+length] = mask_array[:, x:x+length] * 0

    length_list = numpy.array(length_list)
    repetition_measure = ((length_list ** 2).sum()) ** 0.5 / min(s[0], s[1])
    return repetition_measure
    

def get_text_repetition_measure(text_A, text_B, evaluate_func, show_map = False):
    #  生成字块矩阵
    #  字块A，为输入的字符串
    #  字块B，为要比对的文字源
    ##        字 块  A
    ##   字              
    ##   块              
    ##    B              
    
    ##        字 块  A
    ##   字       -      
    ##   块   -   -   -  
    ##    B        -         减号为取消检测的部分
    
    text_A_array = numpy.array(list(text_A), dtype = "object")
    text_B_array = numpy.array(list(text_B), dtype = "object")
    len_A, len_B = [len(text_A_array), len(text_B_array)]

    text_A_matrix = numpy.broadcast_to(text_A_array[numpy.newaxis, :], (len_B, len_A))
    text_B_matrix = numpy.broadcast_to(text_B_array[:, numpy.newaxis], (len_B, len_A))
    
    is_same_array = text_A_matrix == text_B_matrix
    is_same_array = numpy.array(is_same_array, dtype = 'int8')
    
    if show_map:
        print(is_same_array)
    return evaluate_func(is_same_array)

def _api_get_repetition(text_A, text_B)
    return get_text_repetition_measure(text_A, text_B, evaluate_func_A)


if __name__ == "__main__":
    text_A = '宋湜，字持正，京兆长安人。曾祖择，牟平令。祖赞，万年令。父温故，晋天福中进士，至左补阙；弟温舒，亦进士，至职方员外郎，兄弟皆有时名。湜幼警悟，早孤，与兄泌励志笃学，事母以孝闻。温舒典耀州，湜侍行，代作笺奏，词敏而丽。温舒拊背曰：“此儿真国器，恨吾兄不及见也。”太平兴国五年进士，释褐将作监丞、通判梓州榷盐院，就迁右赞善大夫。宋准荐其文，拜著作郎、直史馆，赐绯。雍熙三年，以右补阙知制诰，与王化基、李沆并命，仍赐白金五两、钱五十万。加户部员外郎，与苏易简同知贡举，俄判刑部，赐金紫。淳化二年，道安讼大理断狱不当，湜坐累，降均州团练副使。时母老，湜留其室奉养。移汝州，与王禹偁并召入，为礼部员外郎、直昭文馆。五年，以职方员外郎再知制诰、判集贤院，知银壹、通进。至道元年，为翰林学士，知审官院、三班。真宗即位，拜中书舍人。丁内艰，起复。真宗北巡将次大名以扈从军列为行阵亲御铠甲于中诸王介胄以从命湜与王显分押后阵驻跸数日，常召见便殿，方奏事，疾作仆地。内侍掖出，太医诊视，抚问相继，以疾亟闻。明年正月，真宗临视，许以先归，赐衾褥，曰：“此朕尝御者，虽故暗，亦足御道途之寒。”又遣内侍护送供帐，至澶州，卒，年五十一。废朝，赠吏部侍郎。真宗再幸河朔，追悼之，加赠刑部尚书，谥曰定。湜风貌秀整，有酝藉，器识冲远，好学，美文辞，善谈论饮谑，晓音律，妙于弈棋。笔法遒媚，书帖之出，人多传效。喜引重后进有名者，又好趋人之急，当世士流，翕然宗仰之。有文集二十卷。'
    text_B = '宋湜，字持正，京兆长安人。曾祖择，牟平令。祖赞，万年令。 父温故，晋天福中进士，至左补阙；弟温舒，亦进士，至方员外郎，兄弟皆有时名。湜幼警悟，早孤，与兄泌励志笃学，事母以孝闻。温舒典耀州，湜侍行，代作笺奏，词敏而丽。温舒拊背曰：“此儿真国器，恨吾兄不及见也。”太平兴国五年进士，释褐将作监丞、通判梓州榷盐院，就迁右赞善大夫。宋准荐其文，拜著作郎、直史馆，赐绯。雍熙三年，以右补阙知制诰，与王化基、李沆并命，仍赐白金五百两、钱五十万。加户部员外郎，与苏易简同知贡举，俄判刑部，赐金紫。淳化二年，道安讼大理断狱不当，湜坐累，降均州团练副使。时母老，湜留其室奉养。移汝州，与王禹偁并召入，为礼部员外郎、直昭文馆。五年，以职方员外郎再知制诰、判集贤院，知银壹、通进。至道元年，为翰林学士，知审官院、三班。真宗即位，拜中书舍人。丁内艰，起复。真宗北巡将次大名以扈从军列为行阵亲御铠甲于中诸王介胄从命湜与王显分押后阵驻跸数日，常召见便殿，方奏事，疾作仆地。内侍掖出，太医诊视，抚问相继，以疾亟闻。明年正月，真宗临视，许以先归，赐衾褥，曰：“此朕尝御者，虽故暗，亦足御道途之寒。”又遣内侍护送供帐，至澶州，卒，年五十一。废朝，赠吏部侍郎。真宗再幸河朔，追悼之，加赠刑部尚书，谥曰忠定。湜风貌秀整，有酝藉，器识冲远，好学，美文辞，善谈论饮谑，晓音律，妙于弈棋。笔法遒媚，书帖之出，人多传效。喜引重后进名者，又好趋人之急，当世士流，翕然宗仰之。有文集二十卷。'
    
    time_start = time.time()
    repetition_measure = get_text_repetition_measure(text_A, text_B, evaluate_func_A)

    print("repetition_measure:", repetition_measure, "\ntime used:", time.time() - time_start, "sec.")