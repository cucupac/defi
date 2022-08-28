import matplotlib.pyplot as plt

# INITIAL LIQUIDITY PROVIDED (# OF TOKENS)
X_START = 5
Y_START = 5

# CONSTANTS
K = X_START * Y_START
RANGE = X_START * Y_START

# AUTOMATED MARKET MAKER PRICES
x_list = list(range(1,RANGE))
y_list = [(K / x) for x in x_list]

# X COORDINATES FOR T1, T2, and T3
x_1 = 2
x_2 = 9
x_3 = 16

# PLOT
# CURVE
plt.plot(x_list, y_list)
# T1, T2, and T3 POINTS
plt.plot([x_1], [(K / x_1)], marker="o", markersize=5, markeredgecolor="black", markerfacecolor="black")
plt.text(x_1,(K / x_1), "$T_{1}$ ($x_{1}$,$y_{1}$)")
plt.plot([x_2], [(K / x_2)], marker="o", markersize=5, markeredgecolor="black", markerfacecolor="black")
plt.text(x_2,(K / x_2), "$T_{2}$ ($x_{2}$,$y_{2}$)")
plt.plot([x_3], [(K / x_3)], marker="o", markersize=5, markeredgecolor="black", markerfacecolor="black")
plt.text(x_3,(K / x_3), "$T_{3}$ ($x_{3}$,$y_{3}$)")
# LABELS
plt.title("XYK Pricing Model")
plt.xlabel("Number of X Tokens")
plt.ylabel("Number of Y Tokens")
plt.show()




