"""
比较简单的字符串正则表达式和字节序列正则表达式的行为
"""
import re

if __name__ == "__main__":

    re_numbers_str = re.compile(r"\d+")
    re_words_str = re.compile(r"\w+")
    re_numbers_bytes = re.compile(rb"\d+")
    re_words_bytes = re.compile(rb"\w+")

    text_str = "Ramanujan saw \u0be7\u0bed\u0be8\u0bef"

    text_bytes = text_str.encode('u8')
    print("Text", repr(text_str), sep="\n   ")
    print("Numbers")
    print("  str  :", re_numbers_str.findall(text_str))
    print("  bytes:", re_numbers_bytes.findall(text_bytes))
    print('Words')
    print("  str  :", re_words_str.findall(text_str))
    print("  bytes:", re_words_bytes.findall(text_bytes))
    