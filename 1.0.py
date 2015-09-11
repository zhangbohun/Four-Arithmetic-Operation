# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 10:58:06 2015

@author: zhangbohun
目标:只求代码和实现最优美，当然是我认为的优美咯╮(╯_╰)╭
一时兴起，写写吧
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
    
#当加减遇到乘除或者遇到括号时递归计算
def calculate(list):
    value,i = 0.0,0
    while i < len(list):
        if list[i] in ['+','-']:#加减
            if list[i+1] != '(':
                if i+2 < len(list):
                    if list[i+2] not in ['*','/']:
                        value += list[i+1] if (list[i] == '+') else 0.0-list[i+1]
                        i+=1
                    else:#下一个运算符号为乘除，余下部分全部递归
                        value += calculate(list[i+1:]) if (list[i] == '+') else (0.0 - calculate(list[i+1:]))
                        break
        elif list[i] in ['*','/']:#乘除
            if list[i+1] != '(':
                value *= list[i+1] if (list[i] == '*') else 1.0 / list[i+1]
                i += 1
        elif list[i] == '(':
            j,m=i+1,0
            while(list[j] != ')' or m != 0):#截取()段递归计算
                if list[j] == '(':
                    m += 1
                if list[j] == ')':
                    m -= 1
                j += 1
            if i == 0:
                value += calculate(list[i+1:j+1])
            else:
                if list[i-1] == '+':  
                    value += calculate(list[i+1:j+1])
                elif list[i-1] == '-':
                    value -= calculate(list[i+1:j+1])
                elif list[i-1] == '*':  
                    value *= calculate(list[i+1:j+1])
                elif list[i-1] == '/':
                    value /= calculate(list[i+1:j+1])
            i = j
        elif list[i] == ')':#跳过
            i += 1
        else:
            value += list[i]#开头遇到数值
        i += 1
    return value
    
str = '((-2.5+3*-8+0.5)--9/+9)/(1+1)'
#print eval(str)
#print get_numerical_value(str)
print calculate(get_numerical_value(str))