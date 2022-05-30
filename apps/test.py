#coding: utf-8
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# 自作ライブラリの動作テストコード

from test_module import HERO
# hello_hero = HERO(name="tyanko", age=21, sex="male")
# hello_hero()

testdata = np.linspace(-np.pi, np.pi, 50)
print(np.std(testdata, ddof=1))
