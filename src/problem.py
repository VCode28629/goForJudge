# -*- coding: utf-8 -*-

__author__ = 'VCode'

DEFAULT_TIME_LIMIT = 1000
DEFAULT_MEMORY_LIMIT = 128 * 1024
DEFAULT_SCORE = 10

class TestData(object):
    __slots__ = ('name',
                 'time_limit',
                 'memory_limit',
                 'score')
    def __init__(self, name, id):
        self.name = '%s%d' % (name, id)
        self.time_limit = DEFAULT_TIME_LIMIT
        self.memory_limit = DEFAULT_MEMORY_LIMIT
        self.score = DEFAULT_SCORE

class Problem(object):
    __slots__ = ('name', 
                 'input_file', 
                 'output_file', 
                 'std_io', 
                 'test_data',
                 'test_id')
    def __init__(self, name):
        self.name = name
        self.std_io = False
        self.input_file = '%s.in' % name
        self.output_file = '%s.out' % name
        self.test_id = 0
        self.test_data = []
    def add_test_data(self):
        self.test_id += 1
        self.test_data.append(TestData(self.name, self.test_id))
