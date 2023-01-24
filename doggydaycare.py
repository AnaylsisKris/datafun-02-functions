"""
This file illlustrates some built-in functions,
conditions, and branching.

Always start your file with a docstring.

Each file is a module in Python.
The name of the module is the name of the file without the extension.

"""

import webbrowser  # add some fun

print("Hello!, We'll ask for three temperatures in Celcius.")
print()

temp_string_1 = input("Provide a temperature in Celcius: ")
print()
temp_string_2 = input("Provide a temperature in Celcius: ")
print()
temp_string_3 = input("Provide a temperature in Celcius: ")
print()

# convert strings to numbers
temp_1 = float(temp_string_1)
temp_2 = float(temp_string_2)
temp_3 = float(temp_string_3)

# find the sum
sum = temp_1 + temp_2 + temp_3

# find the average - round to 2 decimal places
average = round(sum / 3, 2)

# find the product
product = temp_1 * temp_2 * temp_3

# find the smallest
smallest = min(temp_1, temp_2, temp_3)

# find the largest
largest = max(temp_1, temp_2, temp_3)

# find the range
range = largest - smallest

# print the results
print(f"The sum is {sum}.")
print(f"The average is {average}.")
print(f"The product is {product}.")
print(f"The smallest is {smallest}.")
print(f"The largest is {largest}.")
print(f"The range is {range}.")
print()

# conditions and branching

utterance1 = "It's below freezing at the Doggy Daycare!"
utterance2 = "It's freezing at the Doggy Daycare!"
utterance3 = "It's above freezing at the Doggy Daycare!"
temp_freezing = 0

if temp_3 < temp_freezing:
    print(utterance1)
elif temp_3 == temp_freezing:
    print(utterance2)
else:
    print(utterance3)
print()

# ask more

str_response = input("Do you want to learn more about puppies? (y/n) ")

if str_response == "y":
    # import webbrowser at the top of the file
    webbrowser.open("https://en.wikipedia.org/wiki/Puppy")
