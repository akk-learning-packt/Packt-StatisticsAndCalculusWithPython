import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def stats(s):
    samples_mean = np.mean(s)
    samples_median = np.median(s)
    q1 = np.percentile(s, 25)
    q2 = np.percentile(s, 75)
    return (samples_mean, samples_median, q1, q2)


def plot_hist(mean, median, q1, q2, title):
    fig, ax = plt.subplots()
    ax.hist(samples, bins=20)
    ax.axvline(x=mean, c="red", label="Mean")
    ax.axvline(x=median, c="black", label="Median")
    ax.axvline(x=q1, c="blue", label="Interquartile")
    ax.axvline(x=q2, c="blue")
    ax.set_title(title)
    ax.legend()
    plt.show()


samples = np.random.normal(size=1000)
s_mean, s_median, q1, q2 = stats(samples)
print(f"\nmean: {s_mean}\nmedian: {s_median}")
print(f"\nq1: {q1}\nq2: {q2}")
plot_hist(s_mean, s_median, q1, q2, title="Normal distribution")

# histogram

# Beta distribution
samples = np.random.beta(2, 5, size=1000)
samples_mean, samples_median, q1, q2 = stats(samples)

print(f"\nsamples_mean: {samples_mean}\nsamples_median: {samples_median}")
print(f"\nq1: {q1}\nq2: {q2}")

# histogram
plot_hist(samples_mean, samples_median, q1, q2, title="Beta Distribution")

# gamma distribution
samples = np.random.gamma(5, size=1000)
s_mean, s_median, q1, q2 = stats(samples)
print(f"\nmean: {s_mean}\nmedian: {s_median}")
print(f"\nq1: {q1}\nq2: {q2}")
plot_hist(s_mean, s_median, q1, q2, title="Gamma Distribution")

df = pd.DataFrame(
    {
        "numerical": np.random.normal(size=5),
        "categorical": ["a", "b", "a", "c", "b"],
        "ordinal": [1, 2, 3, 5, 4],
    }
)

print(f"\n{df}")
print(f"{df.describe()}")
print(f"\n{df.describe(include='all')}")

# boxplot
fig, ax = plt.subplots()
ax.boxplot(np.random.normal(2, 5, size=1000), vert=False, showmeans=True)
plt.show()

df = pd.DataFrame(
    {
        "num": np.random.normal(size=1000),
        "cat": np.random.choice(["a", "b", "c"], size=1000),
        "ord": np.random.choice([1, 2, 3, 4, 5], size=1000),
    }
)
print(f"\n{df.head()}")

a = df.loc[df["cat"] == "a", ["num"]]["num"].to_list()
b = df.loc[df["cat"] == "b", ["num"]]["num"].to_list()
c = df.loc[df["cat"] == "c", ["num"]]["num"].to_list()
all_data = [a, b, c]
labels = ["a", "b", "c"]
fig, ax = plt.subplots()
b_plot = ax.boxplot(
    all_data, vert=False, patch_artist=True, labels=labels  # fill with color
)

# fill with colors
colors = ["blue", "green", "pink"]
for bp in b_plot:
    for patch, color in zip(b_plot["boxes"], colors):
        patch.set_facecolor(color)

# add vertical grid lines
ax.xaxis.grid(True)
ax.set_xlabel("Numerical Values")
ax.set_ylabel("Categorical Values")

plt.show()

sns.boxplot(y="num", x="cat", data=df)
plt.show()
