import os


def filepath(fileDir='common',filename='public.py'):
    """

    :param file: 目录
    :param fialname: 文件名
    :return:
    """
    return os.path.join(
        os.path.dirname(os.path.dirname(__file__)),fileDir,filename)



