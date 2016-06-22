#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys


def mapper(object):
    for line in sys.stdin:
        [src, content] = line.strip('\n').split('\t')
        content_set = set(content.split(' '))
        for word in content_set:
            if len(word) > 0:
                print '\t'.join([word, src, '1'])


def reducer(object):
    def init_word_map(word_map):
        for cat in A_C:
            word_map[cat] = 0.0
        return word_map

    def readin(fields):
        [word, cat, cnt] = fields
        if cat not in word_map:
            word_map[cat] = 1.0
        word_map[cat] += float(cnt)

    def output(word_map):
        if len(word_map) == 0:
            return
        A_B = sum([word_map[cat] for cat in word_map])
        C_D = N - A_B

        for cat in word_map:
            A = word_map[cat]
            B = A_B - A
            C = A_C[cat] - A
            D = C_D - C
            chi_squar = N*(A*D-B*C)**2 / A_C[cat] / A_B / B_D[cat] / C_D
            print '\t'.join(map(str, [cat, current_word, chi_squar, A, B, C, D,
                                      1 if A*D > B*C else -1]))

    A_C = {}
    B_D = {}
    N = 0.0
    ratio_file = 'all_cat_segs_cnt'
    with open(ratio_file, 'r') as f:
        for line in f:
            [cat, cnt] = line.strip('\n').split('\t')
            A_C[cat] = float(cnt)
            N += float(cnt)
    for cat in A_C:
        B_D[cat] = N - A_C[cat]

    current_word = None
    word_map = {}
    for line in sys.stdin:
        [word, src, cnt] = line.strip('\n').split('\t')
        if word != current_word:
            output(word_map)
            current_word = word
            word_map = init_word_map(word_map)

        readin([word, src, cnt])
        current_word = word

    output(word_map)

if __name__ == '__main__':
    if sys.argv[1] == 'm':
        mapper()
    if sys.argv[1] == 'r':
        reducer()
