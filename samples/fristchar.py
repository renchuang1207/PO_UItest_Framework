#!/user/bin/env python
# encoding: utf-8
# @author: renchuang
# @file: fristchar.py
# @time: 2020/10/26 12:29 上午

#返回字符串中第一个不重复的字母和位置 【热度：⭐️⭐️⭐️⭐️⭐️】
def first_char(str):
    d = {}
    for i in range(len(str)):
        # 累计字符的出现次数
        if str[i] in d:
            d[str[i]] += 1
        # 只出现一次，key对应的value就记1次
        else:
            d[str[i]] = 1
    for i in range(len(str)):
        if d[str[i]] == 1:
            return '第一个不重复的字符串是{},索引是{}'.format(str[i], i)
    return "没有不重复的字符串"


if __name__ == '__main__':
    s = "nihaonihao"
    res = first_char(s)
    print(res)