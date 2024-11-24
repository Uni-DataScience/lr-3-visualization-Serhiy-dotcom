import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.

    Returns:
    matplotlib.figure.Figure: The generated figure.
    """
    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=data, x='x', y='y', ax=ax, color="blue", s=50)

    ax.set_xlabel("Variable X", fontsize=12)
    ax.set_ylabel("Variable Y", fontsize=12)
    ax.set_title("Scatter Plot of X vs Y", fontsize=14)

    plt.tight_layout()
    return fig


# Example data
data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})
fig = create_scatter_plot(data)

fig.savefig('plots/scatter_plot.png')
plt.show()
