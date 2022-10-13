from cmath import log, log10


def myfunction():
    return "GreenDS"

def myfunction():
    return "Hello"

def myfirstgreendsfunction():
    return "return of my first function"

def mysecondgreendsfunction():
    return "return of my second function"

def VolWaterContent(c, d, s, om, ts):
    return 0.7919 + 0.001691 * c - 0.29619 * d - 0.000001491 * pow(s, 2) + 0.0000821 * pow(om, 2) + 0.02427 * pow(c, -1) + 0.01113 * pow(s, -1) + 0.01472 * (log(s)) - (0.0000733 * om * c) - (0.000619 * d * c) - (0.001183 * d * om) - (0.0001664 * ts * s)

