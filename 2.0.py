# -*- coding: utf-8 -*-
"""
Created on Mon Sep 07 18:24:41 2015

@author: zhangbohun
上个版本是顺着自己的思路写的，这次的是按照书上的一种方法实现的，比上次的更简洁明了哦
"""
#识别数值,返回识别出数值的原式（list形式）
def get_numerical_value(raw_string):
    list,str_num = [],''
    for i in range(len(raw_string)):
        #读入数值，包括数值的+-.号
        if (raw_string[i] in '.0123456789') or ((raw_string[i] in '+-') and (i==0 or raw_string[i-1] in '+-*/(')):
            str_num += raw_string[i]
            if i == (len(raw_string) - 1):#数值结尾时将数值字符串转换位真正的数值
                list.append(float(str_num))
        else:#读入符号,同时将之前读入的数值字符串转换位真正的数值
            if str_num != '':
                list.append(float(str_num))
                str_num = ''
            list.append(raw_string[i])
    return list
    
#用符号栈和数字栈实现
def calculate(list):
    list.append('@')#辅助符号‘@’
    i = 0
    nums,op=[],['@']#数字栈和符号栈
    while i < len(list):
        if type(list[i]) != type(''):#数值
            nums.append(list[i])
            i+=1
        elif op[-1] in '(@' and list[i] in ')@':#左右括号抵消，首尾‘@’抵消
            op.pop()
            i+=1
        elif op[-1]=='+' and list[i] in '+-)@':#先加
            nums.append(nums.pop()+nums.pop())
            op.pop()
        elif op[-1]=='-' and list[i] in '+-)@':#先减
            nums.append(-nums.pop()+nums.pop())
            op.pop()
        elif op[-1]=='*' and list[i] in '+-*/)@':#先乘
            nums.append(nums.pop()*nums.pop())
            op.pop()
        elif op[-1]=='/' and list[i] in '+-*/)@':#先除
            nums.append(1/nums.pop()*nums.pop())
            op.pop()
        else:#优先级更高，压入符号栈
            op.append(list[i])
            i+=1
    return nums[-1]
    
str = '((-2.5+3*-8+0.5)--9/+9)/(1+1)'
#print eval(str)
#print get_numerical_value(str)
print calculate(get_numerical_value(str))