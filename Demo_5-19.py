"""
函数注释
"""
from inspect import signature


def clip(text: "一大段文字", max_len: 'int > 0' = 80) -> "一小段文字":
    """
    在max_len前面或后面的第一个空格处截断文本
    :param text:
    :param max_len:
    :return:
    """

    end = None
    if len(text) > max_len:
        space_before = text.rfind(" ", 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(" ", max_len)
            if space_after >= 0:
                end = space_after

    if end is None:
        end = len(text)
    return text[:end].rstrip()


if __name__ == '__main__':
    print(clip("aaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaa"))
    sig = signature(clip)
    print(sig.return_annotation)
    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ":", param.name, "=", param.default)
        
