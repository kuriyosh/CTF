#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@file test.py
@brief
@date 2018-11-05
@author Yoshiki Kurihara <y-kurihara@ist.osaka-u.ac.jp
'''
def main():
    str = "ΥΔΗΖΙΝΔJΙ-ΧJΙΟΜJGGΔΙΒ ΑJΜΟ \"ΥJΓ\" ΓΥΝ ΙJΡ WΖΖΙ ΥΖΗJGΔΝΓΖΥ, ΥΙΥ ΟΔΗΖ ΝΟΥΜΟΖΥ ΑGJΡΔΙΒ ΜΖQΖΜΝΖGΤ. \"QΥΠΝ\" ΗΥΙΥΒΖΥ ΟJ ΖΝΧΥΚΖ ΑΜJΗ ΟΓΖ ΥΔΝΟJΜΟΖΥ ΝΚΥΧΖ. WΠΟ ΟΓΖ ΜΖΥG QJΤΥΒΖ JΑ \"ΥΜFΥΙJΔΥ\" ΔΙ ΟΓΖ ΒΥGΥΣΤ ΓΥΝ JΙGΤ ΝΟΥΜΟΖΥ......"
    for s in list(str):
        print("{}: {}".format(s,ord(s)))

if __name__ == '__main__' :
    main()
