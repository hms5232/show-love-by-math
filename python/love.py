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
plt.plot(x,y)
plt.show()