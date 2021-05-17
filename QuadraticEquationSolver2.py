def calculation1():
    answers = []
    for x in range(-c, c + 1):
        if (a * x * x) + (b * x) + c == 0:
            answers.append(x)
    if len(answers) == 0:
        print("The Quadratic Equation is unsolvable.")
    else:
        print(f"The answers are {answers}")

def calculation2():
    answers = []
    for x in range(c, (-1 * c) + 1):
        if (a * x * x) + (b * x) + c == 0:
            answers.append(x)
    if len(answers) == 0:
        print("The Quadratic Equation is unsolvable.")
    else:
        print(f"The answers are {answers}")

while True:
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    if c > 0:
        calculation1()
    else:
        calculation2()
    response = input("Do You Have Another Question? ")
    if response == "yes" or response == "Yes":
        continue
    else:
        break
