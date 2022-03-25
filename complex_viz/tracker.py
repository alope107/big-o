class Tracker:
    def __init__(self):
        self.count = 0
    def add(self, num=1):
        self.count += num
    def reset(self):
        self.count = 0

def track_growth(f, ns, tracker):
    counts = []
    for n in ns:
        tracker.reset()
        f(n, tracker=tracker)
        counts.append(tracker.count)
    return ns, counts