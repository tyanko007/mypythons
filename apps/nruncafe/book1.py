# coding: utf-8

# import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tabulate as tb

class Main:
    def __init__(self):
        self.ramenStore = pd.read_csv("./../../datasets/ramen_data.csv", encoding="utf8")

    def __call__(self):
        print(self.ramenStore["金額"][1:])

    # 階級分の実装(スタージェスの公式を利用した実装も可能にする)
    ## starはスタージェスの公式の利用フラグ(default = false)
    ## sbinsは階級の数を定義(default = 10)
    ## https://numpy.org/doc/stable/reference/generated/numpy.histogram.html
    def separate(self, star=False, sbins=10):
        data = self.ramenStore["金額"]
        if star is True:
            b = round(1 + np.log2(len(data)))
            hist, bins = np.histogram(data, bins=b)
        else:
            hist, bins = np.histogram(data, bins=sbins, )

        result = pd.DataFrame({
            "dosu": hist,
            "kaikyu": bins[:-1],
            "kaikyu_value": (bins[:-1]+bins[1:])/2
        })
        result["soutaidosu"] = hist/len(data)*100
        print(tb.tabulate(result, headers="keys", tablefmt='github', showindex=False))


main = Main()
main.separate()
