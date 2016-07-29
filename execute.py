#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Python 3.5.2 :: Anaconda 4.1.1 (x86_64)
'''

import MeCab
import sample as S
import functions as F


def morphoAnalysis(text):
    m_a = MeCab.Tagger("-Ochasen")
    result = m_a.parse(text)
    #print("#####result#####\n{}".format(result))

    return result

def main():
    text_1 = S.sample_1
    text_2 = S.sample_2
    text_3 = S.sample_3
    text_4 = S.sample_4
    text_5 = S.sample_5

    analysis_1 = morphoAnalysis(text_1)
    print("#{}#".format(text_1))
    print("の形態素解析の結果は以下の通り．\n{}".format(analysis_1))

    model1_2 = F.MorphpAnalysis(text_1, text_2)
    coefficient1_2 = model1_2.coefficient(type = 2)
    print("#{}#\nと\n#{}#\nの係数".format(text_1, text_2))
    print(coefficient1_2)

    model3_4 = F.MorphpAnalysis(text_3, text_4)
    coefficient3_4 = model3_4.coefficient()
    #print(coefficient3_4)


if __name__ == "__main__":
    main()
