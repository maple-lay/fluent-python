"""
从定位参数到仅限关键字参数
"""

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
    print(tag('br'))
    print('p', 'hello')
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))
    print(tag('p', 'hello', 'world', cls='sidebar'))
    print(tag(content='testing', name='img'))
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jgp', 'cls': 'framed'}
    print(tag(**my_tag))