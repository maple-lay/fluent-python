"""
Unicode数据库

正则re对于Unicode并不完美适配，有新的regex模块
"""

import unicodedata
import re

if __name__ == "__main__":
    re_digit = re.compile(r"\d")
    sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
    for char in sample:
        print('U+%04x' % ord(char),
              char.center(6),
              're_dig' if re_digit.match(char) else "-",
              'isdig' if char.isdigit() else "-",
              "ifnum" if char.isnumeric() else "-",
              format(unicodedata.numeric(char), "6.2f"),
              unicodedata.name(char),
              sep="\t"
              )