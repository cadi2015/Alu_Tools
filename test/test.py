#!/usr/bin/python
# -*- coding: UTF-8 -*-
from utils import printWithChinese

book_dict = {"price": 500, "bookName": "Python设计", "weight": "250g"}

printWithChinese(book_dict)

book_dict["owner"] = "tyson" #第一种方式，指定key，并且为其赋值一个value，如果key存在，就是修改value，反之就添加一个Entry

printWithChinese(book_dict)

book_dict.update({"country": "china"}) #第二种方式，使用update方法,传入一个字典进去，如果key存在，就会覆盖掉原有的value，反之就是添加一个或多个Entry进入
                                       #多个Entry的情况，取决于你的字典里有多少个Entry嘛，哈哈，明白里吧
printWithChinese(book_dict)

book_dict.update(temp = "无语中", help = "帮助") #第三种方式，直接传一个以key为变量进去，如果存在同样是修改value，不存在，就是添加一个或多个Entry进去

printWithChinese(book_dict)


                            #注意，字典中的Entry是无序的