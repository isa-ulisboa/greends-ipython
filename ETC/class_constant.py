# Define constants within a class to stress that they are constant values not to overwrite
# This, however, doesn't prevent from reassigning the value with e.g. Constants.RISK=1
class Constants():
    YEARS=20
    RATE=0.04
    RISK=0.01

print(Constants.RISK) # prints 0.1