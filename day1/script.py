'''
Day 1: Hello, World!
Filename: script.py
Description: A simple Python script that prints "Hello, World!" to the console.
             And performs basic tasks to showcase Python syntax.
Date: October 25, 2025
Author: Phillip Bridgeman
Version: 1.0.0
Copyright: © 2025 Phillip Bridgeman. All rights reserved.
'''

# Task 1: Print "Hello, World!" to the console
print("Hello, World!")

# Task 2.a: Use of escape characters to create new lines betweens lines of Hello World.
print("Hello, World!\nHello, World!\nHello, World!")

# Task 2.b: Use string concatenation to combine "Hello", " ", and "World!" into a single string and print it.
print("Hello" + " " + "World!")

# Task 3: Use of input function to get user's name and greet them.
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Day 1 of 100 Days of Python Projects.")

# Task 4.a: Use of variables and other functions within a formatted string.
name = "Pillip"
print (name)
name = "Bridgeman"
print(name)

# Task 4.b: Use of len function to determine the length of a string and print it.
username = input("Enter your name: ")
length = len(username)
print(f"Your name has {length} characters.")

'''
Rules for creating variable names in Python:
1. Variable names must start with a letter or an underscore (_).
2. Variable names can contain letters, numbers, and underscores.
3. Variable names are case-sensitive (e.g., myVar and myvar are different variables).
4. Avoid using Python keywords (e.g., def, class, if) as variable names.
'''

'''
Final Project: Band Name Generator
'''
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in? \n")
pet = input("What's your pet's name? \n")
print(f"Your band name could be {city} {pet}!")