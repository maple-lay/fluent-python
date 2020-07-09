"""
比较 规范化Unicode字符串
"""
from unicodedata import normalize


def nfc_equal(str_1, str_2):
    return normalize("NFC", str_1) == normalize("NFC", str_2)


def fold_euqal(str_1, str_2):
    return (normalize("NFC", str_1).casefold() ==
            normalize("NFC", str_2).casefold())


if __name__ == '__main__':
    print(nfc_equal("café", "cafe\u0301"))
    print(fold_euqal("café", "cafe\u0301"))
    