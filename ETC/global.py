# example of declaration of global variable
x = 1

def main():
    global x # if missing, UnboundLocalError: local variable 'x' referenced before assignment
    x+=1
    print(x) # prints 2

if __name__ == "__main__":
    main()

