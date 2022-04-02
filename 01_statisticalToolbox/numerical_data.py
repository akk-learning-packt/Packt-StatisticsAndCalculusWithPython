# Normalization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# mean = 4, sd = 10
samples = np.random.normal(4, 10, size=1000)
plt.hist(samples, bins=20)
plt.show()

# centre the data aroun 0, lies between -3 and 3
normalized_samples = (samples - 4) / 10
plt.hist(normalized_samples, bins=20)
plt.show()

sample_mean = np.mean(samples)
sample_sd = np.std(samples)
print(f"\nsample_mean: {sample_mean}\nsample_sd: {sample_sd}")

# min max scaling

df = pd.read_csv("../data/data.csv")
print(f"\n{df.head()}")


def min_max_scale(data, a, b):
    data_max = np.max(data)
    data_min = np.min(data)
    return a + (b - a) * (data - data_min) / (data_max - data_min)


plt.hist(df["Column 1"], bins=20)
plt.show()

plt.hist(min_max_scale(df["Column 1"], -3, 3), bins=20)
plt.show()
