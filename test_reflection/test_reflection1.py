# coding: UTF-8

'''
反射的简单含义：

　　通过类名获得类的实例对象

　　通过方法名得到方法，实现调用
'''

from person import Person
print globals()

raw_input("input to continue")
theObj = globals()["Person"]()
print theObj.getName()

raw_input("input to continue")
p2 = Person()
print p2.getName()