"""
Unicode标准:字符的标识和具体的字节表述

    字符的标识，即码位
    字符的具体表述取决于所用的编码

    把码位转换成字节序列的过程是编码；把字节序列转换成码位的过程是解码
"""

if __name__ == '__main__':
    str_a = 'cafe'
    print(len(str_a))
    b = str_a.encode("utf-8")
    print(b)
    str_b = b.decode("utf-8")
    print(str_b)

    print("分隔线\n---------------------------------------------")
    print()
    cafe = bytes("cafe", encoding='utf-8')
    print(cafe)
    print(cafe[0])
    print(cafe[:1])
    cafe_arr = bytearray(cafe)
    print(cafe_arr)
    print(cafe_arr[-1])

    dd = bytes.fromhex('21 3b 19 25')
    str_d = dd.decode('utf-8')
    print(dd)
    print(str_d)
