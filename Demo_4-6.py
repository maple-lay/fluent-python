"""
处理UnicodeEncodeError

处理UnicodeDecodeError

如何找出字节系列的编码
    Chardet库

"""

if __name__ == '__main__':

    # 获取一个特殊字符
    diff_char = b"\xc3\xa3".decode('utf8')
    print(diff_char)

    str_a = "s"+diff_char+"o Paulo"
    print(str_a)
    # str_a.encode('cp437')  # 报错
    # UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>
    print(str_a.encode('cp437', errors='ignore'))  # 跳过
    print(str_a.encode('cp437', errors='replace'))  # 把错误数据换成“？”
    print(str_a.encode('cp437', errors='xmlcharrefreplace'))  # 无法编码的字符替换成XML实体

    octets = b"Montr\xe9al"
    print(octets.decode('cp1252'))
    print(octets.decode('iso8859_7'))
    print(octets.decode('koi8_r'))
    # octets.decode('u8')  报错
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte
    print(octets.decode('u8', errors='replace'))

