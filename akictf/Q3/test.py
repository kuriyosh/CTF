#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@file test.py
@brief
@date 2018-11-05
@author Yoshiki Kurihara <y-kurihara@ist.osaka-u.ac.jp
'''
def main():
    test = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            '0','1','2','3','4','5','6','7','8','9','+','/','=']
    str = "rKrUl+/clKHb4u/sm6sgnaPfnO/XkO=ewqPU45bRjp4gwa7NntoM467Onu/enqPRlakgj6Egjp0e1gAA"

    ans = ""
    for s in list(str):
        ans += test[len(test)-test.index(s)-1]
        print(test[len(test)-test.index(s)-1])

    print(ans)

if __name__ == '__main__' :
    main()
