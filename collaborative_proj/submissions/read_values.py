def read_values():
    values = []
    for i in range(25):
        values.append(10 + (i * i * 13 + i * 5 + 7) % 37 % 11)
    return values
