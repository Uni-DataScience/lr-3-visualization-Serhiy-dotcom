import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_1d(data):
    """
    Create a 1D line plot for a sequence of values.

    Parameters:
    data (array-like): Sequence of values to plot.
    """
    plt.figure()
    plt.plot(data, label='1D Line')
    plt.title('1D Line Plot')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.grid()
    plt.savefig('plots/1d_plot.png')
    plt.show()


def plot_2d(x, y):
    """
    Create a 2D scatter plot for two variables.

    Parameters:
    x (array-like): X-axis values.
    y (array-like): Y-axis values.
    """
    plt.figure()
    plt.scatter(x, y, c='blue', alpha=0.7, edgecolors='k', label='2D Scatter')
    plt.title('2D Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid()
    plt.savefig('plots/2d_plot.png')
    plt.show()


def plot_3d(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=z, cmap='viridis', label='3D Scatter')
    ax.set_title('3D Scatter Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    plt.legend()
    plt.savefig('plots/3d_plot.png')
    plt.show()


# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)
