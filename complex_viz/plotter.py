from .tracker import track_growth

from matplotlib import pyplot as plt

def plot_growth(f, ns, ticks=None):
    x, y = track_growth(f, ns)
    if ticks is not None:
        x = ticks
    plt.plot(x, y, label=f.__name__)


def compare_growth(fs, ns, ticks=None):
    for f in fs:
        plot_growth(f, ns, ticks=ticks)
    plt.legend(loc="upper left")