# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 20:30:15 2015

@author: zhangbohun
想起当年编译原理课，用ll(1)文法分析实现了一下
"""
#识别数值(就相当于词法分析吧),返回识别出数值的原式（list形式）
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
    
#四则运算式的ll(1)语法
'''
E -> TE'
T -> FT'
E' -> +TE' | -TE' | empty
T' -> *FT' | /FT' | empty
F -> (E) | V
'''
i=0 #全局变量          
def E(list):
    return T(list)+E_(list)
    
def T(list):
    return F(list)*T_(list)
    
def E_(list):
    global i
    if i+1<len(list):
        i+=1
        if list[i]=='+':
            if i+1<len(list):
                i+=1
                return T(list)+E_(list)
        elif list[i]=='-':
            if i+1<len(list):
                i+=1
                return -(T(list)-E_(list))
        else:
            i-=1
            return 0
    else:
        return 0
        
def T_(list):
    global i
    if i+1<len(list):
        i+=1
        if list[i]=='*':
            if i+1<len(list):
                i+=1
                return F(list)*T_(list)
        elif list[i]=='/':
            if i+1<len(list):
                i+=1
                return 1/(F(list)/T_(list))
        else:
            i-=1
            return 1
    else:
        return 1
        
def F(list):
    global i
    if i<len(list):
        if list[i]=='(':
            if i+1<len(list):
                i+=1
                val = E(list)
                if i+1<len(list):
                    i+=1
                    if list[i]==')':
                        return val
        elif type(list[i]) != type(''):#数值
            return list[i] 
            
def calculate(list):
    return E(list)
    
str = '((-2.5+3*-8+0.5)--9/+9)/(1+1)'
#print eval(str)
#print get_numerical_value(str)
print calculate(get_numerical_value(str))