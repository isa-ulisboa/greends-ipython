import random

# global variables:
N=10 # number of problems
T=3 # maximum number of tries

def main():
    level=get_level()
    count_correct=0
    for i in range(N):
        # create problem
        prompt,correct_answer=generate_prompt(level)
        # prompt for answer: the output can be True (correct answer within T tries) or False (otherwise)
        correct=get_answer(prompt,correct_answer,T)
        # update number of correct answers or provide the correct answer
        if correct:
            count_correct += 1
        else:
            print(prompt,correct_answer)
    # print score
    print("Score:", count_correct)

# input: void
# output: integer (user provided integer between 1 and 3)
def get_level():
    ...
            return(level)

# input: integer (level)
# output: string (prompt for the user, e.g. '3 + 8 = '), integer (correct answer, e.g. 11)
def generate_prompt(level):
    ...
    return prompt, correct_answer

# input: integer (level)
# output: integer (random number between 0 and 9, or between 10 and 99 or between 100 and 999)
def generate_integer(level):
    ...

# input: string (prompt for user), integer (correct answer), integer (T=maximum number of tries)
# output: boolean (True is the answer is correct within T tries, and False otherwise) 
def get_answer(prompt,n,T):
    tries=0
    while tries<T:
        ...

# input: string (prompt to user), integer (minimum value for input), integer (maximum value for input)
# output: integer (user's provided integer between minimum and maximum)
def get_integer(prompt,Min, Max):
    ...
                return x


# main
if __name__ == "__main__":
    main()
