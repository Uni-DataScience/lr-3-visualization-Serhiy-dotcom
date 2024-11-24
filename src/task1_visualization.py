import matplotlib.pyplot as plt
import numpy as np
import collections


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.

    Returns:
    matplotlib.figure.Figure: The generated figure.
    """
    counter = collections.Counter(data)
    categories = list(counter.keys())
    frequencies = list(counter.values())

    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(categories, frequencies, color=['blue', 'green', 'orange'])

    ax.set_xlabel("Category", fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    ax.set_title("Frequency of Categorical Data", fontsize=14)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            str(height),
            ha='center',
            va='bottom',
            fontsize=10
        )

    plt.tight_layout()
    return fig


# Example data
data = np.random.choice(['A', 'B', 'C'], size=100)
fig = plot_distribution(data)

# Save the plot to the 'plots' folder
fig.savefig('plots/bar_chart.png')
plt.show()
