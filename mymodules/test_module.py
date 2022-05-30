# coding: utf-8
import numpy as np
import pandas as pd

#モジュールのテスト用コード

class HERO:
    def __init__(self, name=None, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex

    def __call__(self):
        print("Hi, " + self.name + ".Welcome to HeroProjectTeam!!")
        if self.age is None or self.age <= 0:
            print("Invalid age status.")
        else:
            print("your old is " + str(self.age), "your sex is " + self.sex)
