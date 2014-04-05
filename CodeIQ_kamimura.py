#!/usr/bin/env python
#-*- coding:utf-8 -*-


# 解答の関数
def ja2enCountryName(name):
    # 関数の本体、解答を記述する部分
    list = {
        "日本": "Japan",
        "米国": "America",
        "英国": "Britain",
        "仏国": "France",
        "露国": "Russia",
        "中国": "China",
    }
    if name in list:
        return list[name]
    else:
        return "?"


for name in ['日本', '米国', '英国', '仏国', '露国', '中国', '宇宙']:
    print(ja2enCountryName(name))
