#Chapter4/Example21.py
#!/usr/bin/python  #(说明python解释器)
#coding:utf-8  #(采用中文编码)
point=int(input("请输入你的分数:"))
    if point>=90:
        print("你的等级是A")
    elif point>=75:
        print("你的等级是B")
    elif point>=60:
        print("你的等级是C")
    else:
        print("恭喜你，不及格")
#也可以用下面这种写法
try:
    point=int(input("请输入你的分数:"))
    if point>=90:
        print("你的等级是A")
    elif point>=75:
        print("你的等级是B")
    elif point>=60:
        print("你的等级是C")
    else:
        print("恭喜你，不及格")
except ValueError:
    print("小盆友，你确定这是你的成绩?")
