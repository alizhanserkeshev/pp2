import math
import itertools 
import random

#Task 1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

#Task 2
def fahrenheit_to_centigrade(fahrenheit):
    centigrade = (5/9) * (fahrenheit-32)
    return centigrade

#Task 3
def solve(numheads, numlegs):
    num_chickens = (2 * numheads - numlegs) / 2
    num_rabbit = numheads - num_chickens
    return num_chickens, num_rabbit

#Task 4
def filter_prime(numbers):
    def prime(n):
        if n < 2:
            return 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % 1 == 0:
                return 0
        return 1
    return[num for num in numbers if prime(num)]

#Task 5
def permutation(str):
    return list(itertools.permutation(str))

#Task 6
def reverse(sentence):
    words = sentence.split()
    reversedsen = ' '.join(reversed(words))
    return reversedsen

#Task 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return true
    return false

#Task 8
def spy_game(nums):
    pattern = [0, 0, 7]    
    index = 0
    for num in nums:
        if num == pattern[index]:
            index += 1
            if index == len(pattern):
                return true
    return false 

#Task 9
def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

#Task 10
def unique_elements(list):
    unique_list = []
    for elem in list:
        if elem not in unique_list:
            unique_list.append(elem)
    return unique_list

#Task 11
def ispaindrome(word):
    return word == word[::-1]

#Task 12
def histogramm(numbers):
    for num in numbers:
        print('*' * num)

#Task 13
def guess_the_number():
    number_to_guess = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    guesses_taken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break


