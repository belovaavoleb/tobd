import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns



rat = np.load('average_ratings.npy')

first_gr = plt.figure()
ax = first_gr.add_axes([0.1, 0.1, 0.8, 0.8])
x = [i for i in range(1095)]
# 1 задание
# firstline, = ax.plot(x, rat[0], 'orange', label = 'waffle iron french toast')
# secondline, = ax.plot(x,rat[1], 'olive', label = 'zwetschgenkuchen bavarian plum cake')
# thirdline, = ax.plot(x, rat[2], 'purple', label = 'lime tea')
# ax.set_title("Change of the ranges")
# ax.legend(handles=[firstline, secondline, thirdline], loc = 'upper left')
# ax.set_xlabel("Numder of the day")
# ax.set_ylabel("Range of recipes")
# ax.grid(color='blue', alpha=0.2)
# plt.show()


# 2 задание
# date = pd.date_range(start='1/1/2019', end='30/12/2021')
# firstline, = ax.plot(date, rat[0], 'orange', label = 'waffle iron french toast')
# secondline, = ax.plot(date,rat[1], 'olive', label = 'zwetschgenkuchen bavarian plum cake')
# thirdline, = ax.plot(date, rat[2], 'purple', label = 'lime tea')
# ax.set_xlabel("Date")
# ax.set_title("Change of the ranges")
# ax.set_ylabel("Range of recipes")
# ax.legend(handles=[firstline, secondline, thirdline], loc = 'upper left')
# ax.set_xlim([date[0], date[-1]])
# ax.xaxis.set_major_locator(mdates.YearLocator())
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
# plt.show()


# 3 задание
# dates = pd.date_range(start='1/1/2019', end='30/12/2021')
# fig2, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize = (9, 9), sharex='col')
# fig2.suptitle("Change of the ranges")
#
# ax1.plot(dates, rat[0], 'orange', label = 'waffle iron french toast')
# ax1.set_xlim([dates[0], dates[-1]])
# ax1.xaxis.set_major_locator(mdates.YearLocator())
# ax1.xaxis.set_minor_locator(mdates.MonthLocator())
# ax1.grid(color='blue', alpha=0.2)
# ax1.legend()
#
# ax2.plot(dates, rat[1], 'olive', label = 'zwetschgenkuchen bavarian plum cake')
# ax2.set_xlim([dates[0], dates[-1]])
# ax2.xaxis.set_major_locator(mdates.YearLocator())
# ax2.xaxis.set_minor_locator(mdates.MonthLocator())
# ax2.grid(color='slateblue', alpha=0.2)
# ax2.legend()
#
# ax3.plot(dates, rat[2], 'purple', label = 'lime tea')
# ax3.set_xlabel("Date")
# ax3.set_xlim([dates[0], dates[-1]])
# ax3.xaxis.set_major_locator(mdates.YearLocator())
# ax3.xaxis.set_minor_locator(mdates.MonthLocator())
# ax3.legend(loc='upper left')
# ax3.grid(color='slateblue', alpha=0.2)
# plt.show()



# 4 задание
# v = np.load('visitors.npy')
# f3, (x1, x2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
# f3.suptitle('Change in number of users at linear and logarithmic scales')
#
# x1.plot(np.arange(1,101), v, label='$y(x)=\lambda e^{-\lambda x}$')
# x1.set_xlabel("Number of days since promotion")
# x1.set_ylabel("Number of visitors")
# x1.plot(np.arange(1,101), [100]*100, 'r', label='$y(x)=100$')
# x1.legend()
# x1.grid(color='blue', alpha=0.2)
#
# x2.plot(np.arange(1,101), v, label='$y(x)=\lambda e^{-\lambda x}$')
# x2.set_yscale('log')
# x2.set_xlabel("Number of days since promotion")
# x2.set_ylabel("Number of visitors")
# x2.plot(np.arange(1,101), [100]*100, 'r', label='$y(x)=100$')
# x2.legend()
# x2.grid(color='blue', alpha=0.2)
# plt.show()


