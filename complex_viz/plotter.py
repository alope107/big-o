from .tracker import track_growth

from matplotlib import pyplot as plt

def plot_growth(f, ns):
    x, y = track_growth(f, ns)
    plt.plot(x, y, label=f.__name__)


def compare_growth(fs, ns):
    for f in fs:
        plot_growth(f, ns)
    plt.legend(loc="upper left")