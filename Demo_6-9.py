"""
使用函数作为对象，替换"命令"模式
"""


class MacroCmomand:
    """
    一个执行一组命名的命令
    """
    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self, *args, **kwargs):
        for command in self.commands:
            command()