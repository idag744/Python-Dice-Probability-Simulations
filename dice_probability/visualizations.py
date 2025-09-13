import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(data, title="Histogram of Dice Rolls"):
    sns.histplot(data, bins=int(max(data)-min(data)+1), discrete=True)
    plt.title(title)
    plt.xlabel("Sum of Rolls")
    plt.ylabel("Frequency")
    plt.show()

def plot_pmf(pmf, title="Probability Mass Function"):
    plt.bar(pmf.keys(), pmf.values())
    plt.title(title)
    plt.xlabel("Sum of Rolls")
    plt.ylabel("Probability")
    plt.show()

