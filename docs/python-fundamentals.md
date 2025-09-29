# Python Fundamentals - Core Concepts & Mental Models

This notebook teaches Python syntax through **mental models** - the fundamental thinking patterns that help you solve real problems. When you encounter a scenario, you'll know exactly which tool to reach for.

## Learning Path Overview

1. **Basic Data Types** - The building blocks (numbers, text, true/false)
2. **Collections** - Containers for multiple items (lists, dictionaries)  
3. **Indexing** - How to grab specific items from containers
4. **String Operations** - Working with text data
5. **Conditional Logic** - Making decisions in your code
6. **Functions** - Reusable code blocks for specific tasks
7. **For Loops** - Repeating actions on multiple items
8. **Error Handling** - Gracefully dealing with problems
9. **Main Pattern** - Organizing code for reuse vs direct execution
10. **Intermediate Concepts** - Advanced tools for complex problems
11. **Core Programming Activities** - How concepts work together in real applications

## 1. Basic Data Types

**Mental Model**: The building blocks - like different types of containers for storing information.

- **Numbers** (int, float) - For counting, measuring, calculations
- **Strings** - For text, names, messages
- **Booleans** - For yes/no, true/false decisions

**When to use**: Store single pieces of information (age=25, name="John", is_active=True).

```python
# Integer and float numbers
age = 25
height = 5.9
print(f"Age: {age}, Height: {height}")

# String data type
name = "Alice"
message = 'Hello, World!'
print(f"Name: {name}, Message: {message}")

# Boolean values
is_student = True
has_job = False
print(f"Is student: {is_student}, Has job: {has_job}")

# Check data types
print(f"Type of age: {type(age)}")
print(f"Type of name: {type(name)}")
print(f"Type of is_student: {type(is_student)}")
```

## 2. Collections: Lists, Tuples, and Dictionaries

**Mental Model**: Think of containers for multiple items.

- **List**: Like a shopping list - items in order, you can add/remove (mutable)
- **Tuple**: Like coordinates (x, y) - fixed items that never change (immutable)  
- **Dictionary**: Like a contact book - look up info by name (key-value pairs)

**When to use**: Lists for ordered items, tuples for fixed data, dictionaries for labeled data.

```python
# Lists - ordered, mutable collections
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed list: {mixed_list}")

# Tuples - ordered, immutable collections
coordinates = (10, 20)
colors = ("red", "green", "blue")
print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")

# Dictionaries - key-value pairs
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(f"Person: {person}")
```

## 3. Indexing and Accessing Items

**Mental Model**: Like pointing to specific items in a container.

- **Lists/Tuples**: Use position numbers (0, 1, 2...) to grab items
- **Dictionaries**: Use labels (keys) to grab values
- **Slicing**: Grab a range of items at once

**When to use**: When you need specific items from your data, not all of it.

```python
# List indexing (0-based)
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print(f"First fruit: {fruits[0]}")  # apple
print(f"Last fruit: {fruits[-1]}")  # kiwi
print(f"Second fruit: {fruits[1]}")  # banana

# List slicing [start:end:step]
print(f"First three fruits: {fruits[0:3]}")  # ['apple', 'banana', 'orange']
print(f"Every other fruit: {fruits[::2]}")  # ['apple', 'orange', 'kiwi']
print(f"Last two fruits: {fruits[-2:]}")  # ['grape', 'kiwi']

# Tuple indexing (same as lists)
coordinates = (10, 20, 30)
print(f"X coordinate: {coordinates[0]}")  # 10
print(f"Y coordinate: {coordinates[1]}")  # 20

# Dictionary access by key
person = {"name": "John", "age": 30, "city": "New York"}
print(f"Name: {person['name']}")  # John
print(f"Age: {person['age']}")  # 30
print(f"City: {person.get('city', 'Unknown')}")  # New York
print(f"Country: {person.get('country', 'Unknown')}")  # Unknown
```

## 4. String Operations

**Mental Model**: Text is like a chain of characters you can manipulate.

- **Concatenation**: Link text together (+)
- **Methods**: Built-in tools to clean, format, and modify text
- **Formatting**: Insert variables into text templates

**When to use**: Working with user input, file names, messages, or any text data.

```python
# String concatenation and formatting
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# String methods
text = "  Hello, World!  "
print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")
print(f"Lowercase: '{text.lower()}'")
print(f"Uppercase: '{text.upper()}'")
print(f"Replace: '{text.replace('World', 'Python')}'")

# String formatting
age = 25
name = "Alice"
print(f"My name is {name} and I am {age} years old")
print("My name is {} and I am {} years old".format(name, age))

# String indexing and slicing
text = "Python"
print(f"First character: {text[0]}")  # P
print(f"Last character: {text[-1]}")  # n
print(f"First 3 characters: {text[:3]}")  # Pyt
```

## 5. Conditional Logic (if/elif/else)

**Mental Model**: Like decision trees - "If this is true, do that. Otherwise, do something else."

- **if**: Check one condition
- **elif**: Check another condition if the first was false
- **else**: Do this if nothing else matched

**When to use**: Validating data, checking permissions, choosing different actions based on input.

```python
# Basic if statement
age = 18
if age >= 18:
    print("You are an adult")

# if/else statement
score = 85
if score >= 90:
    grade = "A"
else:
    grade = "B or lower"
print(f"Grade: {grade}")

# if/elif/else statement
temperature = 75
if temperature > 80:
    weather = "Hot"
elif temperature > 60:
    weather = "Warm"
elif temperature > 40:
    weather = "Cool"
else:
    weather = "Cold"
print(f"Weather: {weather}")

# Multiple conditions with logical operators
age = 25
has_license = True
if age >= 18 and has_license:
    print("You can drive")
elif age >= 16 and not has_license:
    print("You can learn to drive")
else:
    print("You cannot drive")

# Checking if item is in a list
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("Apple is in the list")
if "grape" not in fruits:
    print("Grape is not in the list")
```

## 6. Functions

**Mental Model**: Like a recipe - give it ingredients (inputs), it does the work, gives you a result.

- **Parameters**: The ingredients you pass in
- **Return**: The result you get back
- **Reusable**: Use the same recipe many times

**When to use**: When you need to do the same task repeatedly with different inputs (calculate tax, send emails, validate data).

```python
# Simple function without parameters
def greet():
    print("Hello, World!")

greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with multiple parameters and return value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Function with default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))
print(greet_with_title("Johnson", "Dr."))

# Function with keyword arguments
def create_profile(name, age, city="Unknown", country="Unknown"):
    return f"Name: {name}, Age: {age}, City: {city}, Country: {country}"

profile = create_profile("John", 30, country="USA")
print(profile)

# Function that returns multiple values
def get_name_parts(full_name):
    parts = full_name.split()
    return parts[0], parts[-1]  # first name, last name

first, last = get_name_parts("John Doe")
print(f"First: {first}, Last: {last}")
```

## 7. For Loops

**Mental Model**: Like going through each item in a list one by one and doing something to each.

- **Iteration**: Go through each item
- **Action**: Do something with each item
- **Comprehension**: Create new lists by transforming old ones

**When to use**: Processing multiple files, sending emails to all users, transforming data in bulk.

```python
# Iterating over a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Using range() for numbers
for i in range(5):
    print(f"Number: {i}")

# Range with start, stop, and step
for i in range(2, 10, 2):
    print(f"Even number: {i}")

# Iterating over a string
word = "Python"
for letter in word:
    print(f"Letter: {letter}")

# Iterating over dictionary keys and values
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(f"{key}: {person[key]}")

# Iterating over dictionary items
for key, value in person.items():
    print(f"{key}: {value}")

# Using enumerate() to get index and value
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# List comprehension (creating lists with loops)
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# Conditional list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")
```

## 8. Error Handling (try/except)

**Mental Model**: Like having a backup plan when things go wrong.

- **try**: Attempt to do something risky
- **except**: If it fails, handle it gracefully instead of crashing
- **finally**: Always do this cleanup, whether it worked or not

**When to use**: Network requests, file operations, user input validation - anywhere things might fail.

```python
# Basic try/except
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Handling multiple exception types
try:
    number = int("abc")
    result = 10 / number
except ValueError:
    print("Invalid number format")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Using else and finally
try:
    number = int("42")
    result = 10 / number
except ValueError:
    print("Invalid number format")
else:
    print(f"Result: {result}")
finally:
    print("This always runs")

# Catching all exceptions (use sparingly)
try:
    risky_operation = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")

# Raising custom exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")
```

## 9. The `if __name__ == "__main__":` Pattern

**Mental Model**: Like having two modes - "standalone script" vs "imported library".

- **Direct execution**: Run the script directly (like a main program)
- **Import mode**: Import functions from the script (like a library)
- **Main block**: Code that only runs when executed directly

**When to use**: When you want functions that can be imported by other scripts, but also want to test them when run directly.

```python
# Define functions that can be imported
def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

# Main execution block
if __name__ == "__main__":
    # This code only runs when the script is executed directly
    print("Running as main script")
    
    # Example usage
    length = 5
    width = 3
    
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    
    print(f"Rectangle: {length} x {width}")
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")

# This code always runs (when imported or executed directly)
print("This always runs")
```

## 10. Additional Intermediate Concepts

**Mental Model**: Advanced tools for complex problems.

- **Lambda**: Quick one-line functions for simple tasks
- **Comprehensions**: Create lists/dicts/sets in one line
- **Sets**: Collections with no duplicates, good for comparisons
- **File operations**: Read/write data to files
- **JSON**: Standard format for exchanging data

**When to use**: Lambda for simple transformations, comprehensions for creating collections, sets for unique items, files for data persistence, JSON for API data.

```python
# Lambda functions (anonymous functions)
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")

# Filter with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares_dict}")

# Set comprehension
unique_lengths = {len(word) for word in ["hello", "world", "python", "code"]}
print(f"Unique word lengths: {unique_lengths}")

# Working with sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

# File operations
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\nThis is a test file.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(f"File content: {content}")

# Working with JSON
import json
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(f"JSON string: {json_string}")

parsed_data = json.loads(json_string)
print(f"Parsed data: {parsed_data}")
```
