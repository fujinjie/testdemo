# -*- coding: utf-8 -*-
import pytest
import allure

@allure.feature("开始测试Calculator")
class TestCalculator:

    @allure.story("开始测试Calculator加法")
    @pytest.mark.run(order=1)
    def test_calculate_add(self, getCalculator,addTestDatas):
        result = getCalculator.mainFunc(num_1=addTestDatas[0], f=addTestDatas[1], num_2=addTestDatas[2])
        if isinstance(result,float):
            result = round(result,3)
        assert result == float(addTestDatas[3])

    @allure.story("开始测试Calculator除法")
    @pytest.mark.run(order=4)
    def test_calculate_div(self, getCalculator,divTestDatas):
        result = getCalculator.mainFunc(num_1=divTestDatas[0], f=divTestDatas[1], num_2=divTestDatas[2])
        if isinstance(result,float):
            result = round(result,3)
        assert result == float(divTestDatas[3])

    @allure.story("开始测试Calculator减法")
    @pytest.mark.run(order=2)
    def test_calculate_min(self, getCalculator,minTestDatas):
        result = getCalculator.mainFunc(num_1=minTestDatas[0], f=minTestDatas[1], num_2=minTestDatas[2])
        if isinstance(result,float):
            result = round(result,3)
        assert result == float(minTestDatas[3])

    @allure.story("开始测试Calculator乘法")
    @pytest.mark.run(order=3)
    def test_calculate_mul(self, getCalculator,mulTestDatas):
        result = getCalculator.mainFunc(num_1=mulTestDatas[0], f=mulTestDatas[1], num_2=mulTestDatas[2])
        if isinstance(result,float):
            result = round(result,3)
        assert result == float(mulTestDatas[3])


if __name__ == '__main__':
    pytest.main(['-v','-s'])
