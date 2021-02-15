# Generate math questions and solve them automatically!

import math
import random
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.xor
}

def repeat():
    q = input('How many math questions/answers do you want generated?\n>')
    try:
        q = int(q)
        return q
    except ValueError:
        print("Please only use numbers!")
        return repeat()

questions = repeat()

opOptions = ["+", "-", "*", "/", "^"]
file = open('generated.txt', 'a+')
for i in range(questions):
    num1 = random.randint(0, 2147483647)
    num2 = random.randint(0, 2147483647)
    randomOption = random.choice(opOptions)
    op = ops[randomOption]
    result = op(num1, num2)
    print(f"{num1} {randomOption} {num2} = {result}")
    file.write(f"\n{num1} {randomOption} {num2} = {result}")

file.close()
print("Finished.")
