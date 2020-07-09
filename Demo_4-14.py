"""
去掉全部组合记号
"""

import unicodedata
import string


def shave_marks(txt):
    """
    去掉全部变音符号
    :param txt: 待处理的字符串
    :return: 处理后的结果
    """

    normal_txt = unicodedata.normalize("NFD", txt)
    shave_txt = "".join(c for c in normal_txt if not unicodedata.combining(c))
    return unicodedata.normalize("NFC", shave_txt)


def shave_latin_marks(txt):
    """
    把拉丁基字符中的所有变音字符删除
    :param txt: 待处理的字符串
    :return: 处理后的字符串
    """

    normal_txt = unicodedata.normalize("NFD", txt)
    latin_base = False
    keeper = []
    for c in normal_txt:
        if unicodedata.combining(c) and latin_base:
            continue  # 忽略拉丁基字符上的变音字符
        keeper.append(c)
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters

    shaved_txt = "".join(keeper)
    return unicodedata.normalize("NFC", shaved_txt)
