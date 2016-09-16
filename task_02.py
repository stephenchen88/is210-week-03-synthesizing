#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

WORD = 'Spanish'
WORD_LEN = len(WORD)
WORD_START = inquisition.SPANISH.index(WORD)
WORD_END = WORD_START + WORD_LEN
REWORD = 'Flemish'

Flemish = inquisition.SPANISH[:WORD_START] + REWORD + inquisition.SPANISH[WORD_END:]

print Flemish

