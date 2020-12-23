# -*- coding: utf-8 -*-
import pytest
import allure
import yaml
from src.calculator import Calculator


def getTestData():
    path = '/Users/fujinjie/PycharmProjects/testdemo/test/testdata.yml'
    data = yaml.safe_load(open(path))
    return data

@allure.feature("测试Calculator")
class TestCalculator:

    @allure.story("对Calculator进行实例化")
    def setup_class(self):
        self.calculator = Calculator


    @allure.story("开始测试Calculator")
    @pytest.mark.parametrize("num_1,f,num_2,exc", getTestData())
    def test_calculate(self, num_1, f, num_2, exc):
        result = self.calculator().mainFunc(num_1, f, num_2)
        assert result == float(exc)


if __name__ == '__main__':
    datas = getTestData()
    print(datas)
