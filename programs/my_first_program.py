from nada_dsl import *

def nada_main():
    #Define the party
    party1 = Party(name="Party1")

    #Define the Secret inputs
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))  # Current salary
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))  # Proposed new salary

    # Calculate the difference
    salary_difference = my_int1 - my_int2

    # Check if there's an increase
    is_increase = my_int2 > my_int1

    return [
        Output(salary_difference, "salary_difference", party1),
        Output(is_increase, "is_increase", party1)
    ]