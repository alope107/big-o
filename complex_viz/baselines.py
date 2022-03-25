from math import log2
from math import factorial as mathfac

def linear(n, tracker):
    tracker.add(n)

def quadratic(n, tracker):
    tracker.add(n**2)

def cubic(n, tracker):
    tracker.add(n**3)

def log(n, tracker):
    if n > 0:
        tracker.add(log2(n))

def nlogn(n, tracker):
    if n > 0:
        tracker.add(n*log2(n))

def factorial(n, tracker):
    tracker.add(mathfac(n))