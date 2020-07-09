"""
    即使某个键不在映射中，也能通过它读取到默认值。
    方法一：
    使用defaultdict方法
    方法二：
    自己创建一个dict的子类，实现__missing__方法

"""

import sys
import re
import collections

WORD_RE = re.compile(r"\w+")
index = collections.defaultdict(list)  # 把list构造方法作为default_factory来创建一个defaultdict

if __name__ == "__main__":
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                locations = (line_no, column_no)
                index[word].append(locations)

    for word in sorted(index, key=str.upper):
        print(word, index[word])
