
val1 = int(1.2)
val2 = ("carlos")
val3 = [13452345,23452345,33452345,43452345,53452345]

def my_function():
    val2_cap= val2.capitalize()
    val3_length = len(val3)
    for i in val3:
        if i == val3[0]:
            print ("O",val2_cap, "tem", val3_length, "cartões,",val1, "com o nuemro", i)
            continue
        print ("outro com o numero", i)

my_function()