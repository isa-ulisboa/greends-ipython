def determine_frequency(x, left, right):
    freq = 0
    for value in x:
        if left <= value < right:
            freq += 1
    return freq
