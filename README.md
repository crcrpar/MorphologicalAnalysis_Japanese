# Morphological Analysis for Japanese text

This is so simple program to analyze morphological of Japanese sentences and compute common 3 similarity coefficients: *Jaccard, Dice, Simpson*.

<!-- Be careful that your text encoding is **utf-8**.-->

## Requirement
- MeCab

## How To Use
I wrote sample sentences to analyze in `sample.py` like below.
```sample.py
# -*- coding: utf-8
sample_1 = "今日は夏休み前日です．今日中にレポートを仕上げなければなりません．"
sample_2 = "明日から冬休みです．クリスマスの予定はバイトです．"
```

This program can be used to calculate similarity coefficients between 2 sentences.
In addition to this, you need to prepare 2 sentences before initialize an instance.
