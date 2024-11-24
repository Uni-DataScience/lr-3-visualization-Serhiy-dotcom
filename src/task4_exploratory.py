import os
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    output_dir = "eda_outputs"
    os.makedirs(output_dir, exist_ok=True)

    descriptive_stats = df.describe().transpose()
    print("Descriptive Statistics:")
    print(descriptive_stats)

    descriptive_stats.to_csv(f"{output_dir}/descriptive_statistics.csv")

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, orient="h", palette="Set2")
    plt.title("Box Plots for Outlier Detection")
    plt.xlabel("Values")
    plt.savefig(f"{output_dir}/box_plots.png")
    plt.show()

    correlation_matrix = df.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        cbar=True,
        square=True,
        linewidths=0.5
    )
    plt.title("Correlation Matrix Heatmap")
    plt.savefig(f"{output_dir}/correlation_heatmap.png")
    plt.show()

    print("\nCorrelation Matrix:")
    print(correlation_matrix)


# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})

perform_eda(df)
