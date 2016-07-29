#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Python 3.5.2 :: Anaconda 4.1.1 (x86_64)
'''

import MeCab
import sample as S
import functions as F


def main():
    text_1 = S.sample_1
    text_2 = S.sample_2

    model1_2 = F.MorphpAnalysis(text_1, text_2)
    coefficient1_2 = model1_2.coefficient(type = 2)
    print("#{}#\nと\n#{}#\nの係数".format(text_1, text_2))
    print(coefficient1_2)


if __name__ == "__main__":
    main()
