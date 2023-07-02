#!/usr/bin/python3


import math

def factorize_number(number):
    factors = []
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            factors.append(i)
            number = number // i
    if number > 1:
        factors.append(number)
    return factors

def factorize_numbers_file(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines()
        for number in numbers:
            number = int(number.strip())
            factors = factorize_number(number)
            factors_str = ' x '.join(str(factor) for factor in factors)
            print(f"The factors of {number} are: {factors_str}")

# Example usage
factorize_numbers_file('numbers.txt')
