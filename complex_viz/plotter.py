from .tracker import track_growth

from matplotlib import pyplot as plt

def plot_growth(f, ns, tracker):
    x, y = track_growth(f, ns, tracker)
    plt.plot(x, y, label=f.__name__)

def compare_growth(fs, ns, tracker):
    for f in fs:
        plot_growth(f, ns, tracker)
    plt.legend(loc="upper left")