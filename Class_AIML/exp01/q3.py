import matplotlib.pyplot as plt
sales = [120, 135, 150, 160, 145, 170, 180, 175, 160, 155, 140, 130]
months = list(range(1, 13))
plt.plot(months, sales, label="Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.legend()
plt.show()
