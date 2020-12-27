# -*- coding: utf-8 -*-
import pytest
import yaml
import os
from src.calculator import Calculator


def getTestDatas():
    path = os.path.abspath('.')+'/test/testdata.yml'
    data = yaml.safe_load(open(path))
    return data

@pytest.fixture(params=getTestDatas()["add"])
def addTestDatas(request):
    print("开始获取yaml数据")
    yield request.param
    print("获取yaml数据结")

@pytest.fixture(params=getTestDatas()["min"])
def minTestDatas(request):
    print("开始获取yaml数据")
    yield request.param
    print("获取yaml数据结")

@pytest.fixture(params=getTestDatas()["mul"])
def mulTestDatas(request):
    print("开始获取yaml数据")
    yield request.param
    print("获取yaml数据结")

@pytest.fixture(params=getTestDatas()["div"])
def divTestDatas(request):
    print("开始获取yaml数据")
    yield request.param
    print("获取yaml数据结")

@pytest.fixture(scope="module")
def getCalculator():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("计算结束")




# def test_one(addTestDatas):
#      print(f"test_one 测试 ：{addTestDatas}")



if __name__=='__main__':
    datas = getTestDatas()
    print(datas['add'])
    print(datas)