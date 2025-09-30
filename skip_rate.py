from spotify import dataset
import matplotlib.pyplot as plt

skip_rate = []

for user in dataset:
    skip_rate.append(float(user["skip_rate"]))

plt.hist(skip_rate, bins = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], rwidth = 0.5, align = "right", color = "orange")
plt.show()