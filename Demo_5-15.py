"""
在制定长度附近截断字符串的函数
"""
from inspect import signature


def clip(text, max_len=80):
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


def tag(name, *content, cls=None, **attrs):
    """
    生成一个或多个HTML标签
    :param name:
    :param content:
    :param cls:
    :param attrs:
    :return:
    """

    if cls is not None:
        attrs['class'] = cls
    if attrs:
        att_str = " ".join('%s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        att_str = ''
    if content:
        return '\n'.join('<%s %s>%s</%s>' % (name, att_str, c, name) for c in content)
    else:
        return '<%s %s />' % (name, att_str)


if __name__ == '__main__':
    print(clip.__defaults__)
    print(id(clip))
    print(clip.__code__)
    print(clip.__code__.co_varnames)
    print(clip.__code__.co_argcount)

    sig = signature(clip)
    print(sig)
    print(str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ":", name, "=", param.default)

    """
    kind属性的值是_ParamterKind类中的5个值之一
    POSITIONAL_OR_KEYWORD：可以通过定位参数和关键字参数传入的形参（多数Python函数的参数属于此类）。
    VAR_POSITIONAL：定位参数元组。
    VAR_KEYWORD：关键字参数字典。
    KEYWORD_ONLY：仅限关键字参数（Python 3新增）。
    POSITIONAL_ONLY：仅限定位参数
    """

    sig2 = signature(tag)
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jgp', 'cls': 'framed'}
    bound_args = sig2.bind(**my_tag)
    print(bound_args)

    for name, value in bound_args.arguments.items():
        print(name, ":", value)
