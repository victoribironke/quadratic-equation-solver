import math

def main_calculation():
    while True:
        try:
            a = int(input("a = "))
            b = int(input("b = "))
            c = int(input("c = "))
            first_step = (b * b) - (4 * a * c)
            second_step = math.sqrt(first_step)
            third_step = second_step - b
            fourth_step = (-1 * second_step) - b
            first_ans = third_step / (2 * a)
            second_ans = fourth_step / (2 * a)
            if first_ans == second_ans:
                print(f"The answer is {first_ans} twice.")
            else:
                print(f"The answers are {first_ans} and {second_ans}.")
            response1 = input("Do You Have Another Question? ")
            if response1 == "yes" or response1 == "Yes":
                continue
            else:
                break
        except ValueError:
            print("The Quadratic Equation is unsolvable.")
            response1 = input("Do You Have Another Question? ")
            if response1 == "yes" or response1 == "Yes":
                continue
            else:
                break



main_calculation()
