def mySpecialFunction1(arg1=12,arg2=34):
    print(arg1,arg2)
    return "Using my other function " + mySpecialFunction1.__name__ + " using namespaces"

val1 = 23 # assigned variables can be accessed. They become a "property" of this module

val2 = "Hi, I became a 'property' of the module"  # assigned variables can be accessed. They become a "property" of this module

val3 = "Hi, I became another 'property' of the module"  # assigned variables can be accessed. They become a "property" of this module
