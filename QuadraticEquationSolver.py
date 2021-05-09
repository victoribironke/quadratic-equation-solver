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
            fifth_step = third_step / (2 * a)
            sixth_step = fourth_step / (2 * a)
            first_ans = fifth_step
            second_ans = sixth_step
            if first_ans == second_ans:
                print(f"The answer is {first_ans} twice.")
            else:
                print(f"The answer is {first_ans} or {second_ans}.")
            question = input("Do You Have Another Equation? ")
            if question == "Yes" or question == 'yes':
                continue
            else:
                break
        except ValueError:
            print("Quadratic Equation is unsolvable")
            response = input("Do You Have Another Question? ")
            if response == 'yes' or response == "Yes":
                continue
            else:
                break


main_calculation()
