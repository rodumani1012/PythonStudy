# -*- coding: UTF-8 -*-

import numpy as np
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# cmd에서 아래 두개 입력해서 설치.
# pip install numpy (수치, 숫자로 연산할 때 사용하는 라이브러리)
# pip install matplotlib (차트, 플롯, 그래프 등 연산된 결과를 시각화하는 라이브러리)

if __name__ == '__main__':
    x = np.arange(0, 11) 
    print(x)
    y = x

    plt.plot(x, y) # (0, 0) ~ (11, 11) 의 결과를 시각화함.
    plt.show()