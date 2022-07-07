"""
https://babyou.nownews.com/news/life/300009081781/?from=bbfb_p&utm_source=fb&utm_medium=bb&utm_campaign=p&fbclid=IwAR2lIlVqQjFaTM873GwrqqNvPdpm746Bq7CDbtVZRPUdTQCqgSgPQB8ECRE
"""


import numpy as np
import tkinter
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt


x = np.linspace(-1,1,100)
y = ((1 - (x**2))**(1/2)) + (x**2)**(1/3)
y2 = -((1 - (x**2))**(1/2)) + (x**2)**(1/3)  # 等式去平方開根號要加上正負號
plt.plot(x,y)
plt.plot(x,y2)
plt.show()
