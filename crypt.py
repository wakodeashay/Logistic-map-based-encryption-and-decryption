#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:55:37 2021

@author: ashay
"""
"""
getchar() :
    ascii string-"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!/"
    input- index (int)
    ouput- char with index from the ascii string
"""
def getchar(n):
    char="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!/"
    return char[n]
"""
getnumb() :
    ascii string-"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!/"
    input- char from the ascii string (str)
    ouput- index of the char from the ascii string
"""
def getnumb(s):
    char="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!/"
    n=char.index(s)
    return n
"""
interval() :
    input- real number between 0.2 and 0.8
    ouput- the char in whose range input falls
    {Refer baptisa.pdf for details}
"""
def interval(x):
    h=0.009375
    n=int((x-0.2)//h)
    return n
"""
encrypt() :
    input- 2 keys for encryption and message to be encrpyted
    ouput- encrypted message
"""
def encrypt(stringkey,paramkey,initkey):
    b=paramkey
    x0=initkey
    s=stringkey
    charlist=[char for char in s]
    code=[]
    for char in charlist:
        c=0
        while getnumb(char)!= interval(x0) :
            c=c+1
            x=b*x0*(1-x0)
            x0=x
        code.append(c)
        x0=x
    return code
"""
dencrypt() :
    input- 2 keys for dencryption and code to be deciphered
    ouput- original message
"""
def decrypt(code,paramkey,initkey):
    b=paramkey
    x0=initkey
    s=""
    for c in code:
        for i in range(0,c):
            x=b*x0*(1-x0)
            x0=x
        s=s+str(getchar(interval(x)%64))
        x0=x
    return s