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
                return f"The answer is {first_ans} twice."
            else:
                return f"The answer is {first_ans} or {second_ans}."
        except ValueError:
            # Code to print when the question is unsolvable.
            return "Quadratic Equation is unsolvable"

print(main_calculation())
