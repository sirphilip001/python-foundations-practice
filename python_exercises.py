#  Q. 1
def greet(name):
    return f"Hello, {name}!"
 
print(greet("Amina"))   # Hello, Amina!
# ------------------------------------------------------------------------------

# Q. 2 
# Write a function add(a, b) that returns the sum of two numbers.

def add(a, b):
    return a + b
 
print(add(5, 3))
# ------------------------------------------------------------------------------ 

# Q. 3 
# Write a function is_even(n) that returns True if a number is even, False if odd.

def is_even(n):
    return n % 2 == 0
 
print(is_even(3))
# ------------------------------------------------------------------------------

# Q. 4 
# Write a function square(n) that returns the square of a number.
#     Then use it to print the squares of 1 to 5.

def square(n):
    return n ** 2
 
for i in range(1, 6):
    print(square(i))
# ------------------------------------------------------------------------------

# Q. 5 
# Write a function max_of_two(a, b) that returns the larger of two numbers
#     (without using the built-in max()).

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
 
print(max_of_two(1, 4))
# ------------------------------------------------------------------------------


#Q. 6 
# Given the list fruits = ["apple", "banana", "cherry"],
# write code to add "mango" to the end, then print the full list.
 
fruits = ["apple", "banana", "cherry"]
fruits.append('mango')
print(fruits)
# ------------------------------------------------------------------------------

# Q. 7
# Given the list numbers = [5, 12, 8, 3, 20], 
# write code to find and print the largest number using a loop.
numbers = [ 5, 12, 8, 3, 20]
maximum_num = numbers[0]
# Loop through the list to compare each number
for num in numbers:
    if num > maximum_num:
        maximum_num = num
 
#Print the result after the loop finishes
print(maximum_num)
# ------------------------------------------------------------------------------


# 8. Create a dictionary 
# student = {"name": "Amina", "age": 20, "course": "Data Science"}. 
# Write code to print each key and value on its own line.
student = {"name": "Amina", "age": 20, "course": "Data Science"}
for key, value in student.items():
 print(f"{key}: {value}")
# ------------------------------------------------------------------------------

# 9. Given the list numbers = [1, 2, 3, 4, 5, 6], 
# write code to print only the even numbers. 
numbers = [1,2,3,4,5,6] 
for number in numbers: 
    if number % 2 ==0: 
        print(number)
# ------------------------------------------------------------------------------


# 10. Write code that counts how many 
# times the number 3 appears in the list [3, 5, 3, 2, 3, 8].
numbers = [3, 5, 3, 2, 3, 8]
print(numbers.count(3))
# ------------------------------------------------------------------------------


# Q. 11. 
# Given the string text = "  Hello World  ",
# write code to remove the extra spaces and convert it to all lowercase.

text = "  Hello World  "
print(len(text))
 
text_2 = text.strip().lower()
print(text_2)
print(len(text_2))
# ------------------------------------------------------------------------------

# Q 12. 
# Write a function count_letter(word, letter) that counts how many times
# a specific letter appears in a word. Example: count_letter("banana", "a") → 3.
 
def count_letter(word,letter):
    count = 0
    for l in word:
        if l == letter:
            count += 1
    return count
 
print(count_letter("banana", 'a'))
 
# Method 2
def count_letters(word, letter):
    return word.count(letter)
print(count_letters('reversed', 'e'))

# 13. Write a function count_words(sentence) 
# that takes a sentence and returns how many words 
# are in it (hint: use .split()).
def count_words(sentence):
    words = len(sentence.split())
    return words
 
print(count_words("Write a function count_words"))
# ------------------------------------------------------------------------------


# 13. Write a function make_initials(full_name) 
# that takes a name like "John Kamau" and returns "J.K." 
# (hint: split the name, take the first letter of each part).
# define function
def make_initials(full_name):
    # convert full name to initials
    parts = full_name.split()
    initials = ""
    for part in parts:
        if part:
            initials += part[0].upper() + "."
    return initials
 
print(make_initials("John Kamau"))

