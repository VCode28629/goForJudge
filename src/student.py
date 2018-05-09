# -*- coding: utf-8 -*-

__author__ = 'VCode'

class Student(object):
    __slots__ = ('name',
                 'score')
    def __init__(self, name):
        self.name = name
        self.score = {}
