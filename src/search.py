# -*- coding: utf-8 -*-

'''
用来查找当前拥有的比赛、和比赛中的题目、参赛者和测试数据
'''

__author__ = 'VCode'

import os

def search_contests():
    #返回当前拥有的比赛列表
    path = os.listdir('./contests/')
    contests = []
    for p in path:
        if os.path.isdir('./contests/%s' % p):
            contests.append(p)
    return contests

def search_problems(contest):
    #返回比赛的题目列表
    #contest: 比赛名称
    path = os.listdir('./contests/%s/data/' % contest)
    problems = []
    for p in path:
        if os.path.isdir('./contests/%s/data/%s' % (contest, p)):
            problems.append(p)
    return problems

def search_students(contest):
    #返回比赛的参赛人员列表
    #contest: 比赛名称
    path = os.listdir('./contests/%s/source/' % contest)
    students = []
    for p in path:
        if os.path.isdir('./contests/%s/source/%s' % (contest, p)):
            students.append(p)
    return students

def search_test_data(contest, problem):
    #contest: 比赛名称
    #problem: 题目名称
    #返回测试数据名称列表(无后缀名)
    path = os.listdir('./contests/%s/data/%s/' % (contest, problem))
    test_data = []
    for p in path:
        if not os.path.isfile('./contests/%s/data/%s/%s' % (contest, problem, p)):
            continue
        if p[-3:] != '.in':
            continue
        if not ('%s%s' % (p[:-3], '.out') in path):
            continue
        test_data.append(p[:-3])
    return test_data
