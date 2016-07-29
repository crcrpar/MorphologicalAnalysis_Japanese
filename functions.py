# -*- coding: utf-8 -*-

import MeCab


class MorphpAnalysis:
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2

    def word_dic(self, text):
        tagger = MeCab.Tagger("-Ochasen")
        node = tagger.parseToNode(text)

        words = []
        nouns = []
        verbs = []

        while node:
            # pick up a word.
            word = node.surface
            # pick up a part of word.
            part = node.feature.split('.')[0].split(',')[0]

            # add `word` to words(list)
            if word:
                words.append(word)

            if part == "名詞":
                nouns.append(word)
            elif part == "動詞":
                verbs.append(word)

            node = node.next

        g_dic = {"word":words, "noun":nouns, "verb":verbs}
        return g_dic

    def coefficient(self, type = None):
        dic_1 = self.word_dic(self.text1)
        dic_2 = self.word_dic(self.text2)

        if type is None:
            type = 1

        if type == 1:
            set_1 = set(dic_1["noun"])
            set_2 = set(dic_2["noun"])
        elif type == 2:
            set_1 = set(dic_1["noun"] + dic_1["verb"])
            set_2 = set(dic_2["noun"] + dic_2["verb"])
        else:
            set_1 = set(dic_1["word"])
            set_2 = set(dic_2["word"])

        inter = set_1.intersection(set_2)
        len_inter = len(inter)
        union = set_1.union(set_2)
        len_union = len(union)
        len_1 = len(set_1)
        len_2 = len(set_2)

        jaccard = float(len_inter / len_union)
        dice = float(2 * len_inter / (len_1 + len_2))
        simpson = float(len_inter / min(len_1, len_2))

        answer = {"Jaccard":jaccard, "Dice":dice, "Simpson":simpson}

        return answer

    def Jaccard(type):

        return self.coefficient(type = type)["Jaccard"]

    def Dice(type):

        return self.coefficient(type = type)["Dice"]

    def Simpson(type):

        return self.coefficient(type = type)["Simpson"]
