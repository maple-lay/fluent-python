"""
    用SetDefault处理找不到的键
"""
import sys
import re


if __name__ == '__main__':

    WORD_RE = re.compile(r'\w+')
    index = {}
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)

                # 一种不太好的实现方式:
                occurrences = index.get(word, [])
                occurrences.append(location)
                index[word] = occurrences

                # 一种更好的处理方式 Demo_3-4
                index.setdefault(word, []).append(location)

    for word in sorted(index, key=str.upper):
        print(word, index[word])
