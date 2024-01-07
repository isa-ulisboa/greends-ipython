def pack(*args, **kwargs):
    print('Positional (*)',args)
    print('Named (**)',kwargs)
    return args,kwargs

print(pack(1,2,10, num_years=10,rate=0.03))