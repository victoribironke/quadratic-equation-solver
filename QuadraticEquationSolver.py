# Importing the module required.
import math

# Function for the main calculation. No parameters.
def main_calculation():
    # Loop in the function incase the user has another question.
    while True:
        # Try and except, incase a question is unsolvable so as not to return an error.
        try:
            a = int(input("a = "))
            b = int(input("b = "))
            c = int(input("c = "))
            # Steps for the calculation based on the quadratic formula.
            first_step = (b * b) - (4 * a * c)
            second_step = math.sqrt(first_step)
            third_step = second_step - b
            fourth_step = (-1 * second_step) - b
            fifth_step = third_step / (2 * a)
            sixth_step = fourth_step / (2 * a)
            first_ans = fifth_step
            second_ans = sixth_step
            if first_ans == second_ans:
                print(f"The answer is {first_ans} twice.")
            else:
                print(f"The answer is {first_ans} or {second_ans}.")
            # To ask if the user has another question
            question = input("Do You Have Another Equation? ")
            if question == "Yes" or question == 'yes':
                continue
            else:
                break
        except ValueError:
            # Code to print when the question is unsolvable.
            print("Quadratic Equation is unsolvable")
            response = input("Do You Have Another Question? ")
            if response == 'yes' or response == "Yes":
                continue
            else:
                break


main_calculation()


# The code below is a simple form of the one above.

'''
def calc():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    answer = []
    for x in range(-c - 1, c + 1):
        if (a*x*x) + (b * x) + c == 0:
            answer.append(x)
    return f"The answers are {answer}."

print(calc())
'''
