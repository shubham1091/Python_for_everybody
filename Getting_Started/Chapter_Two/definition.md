# Constants

- Fixed values such as numbers, letters, and strings, are colled<br>
  "constants" because their values does not change

- Numeric constants are as you expect

- String constants use single quotes ( ' )<br>
  or double quotes ( " )

```python
>>> print(123)
123
>>> print(98.6)
98.6
>>> print("Hello world!")
Hello world!
```

# Python Reserved Words

- You cannot use reserved words as variable names/ identifiers

| Reserved Word | Reserved Word | Reserved Word | Reserved Word | Reserved Word |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| `False`       | `class`       | `return`      | `is`          | `finally`     |
| `None`        | `if`          | `for`         | `lambda`      | `continue`    |
| `True`        | `def`         | `from`        | `while`       | `nonlocal`    |
| `and`         | `del`         | `global`      | `not`         | `with`        |
| `as`          | `elif`        | `try`         | `or`          | `yield`       |
| `assert`      | `else`        | `import`      | `pass`        | `break`       |
| `except`      | `in`          | `raise`       |               |               |

Note: These are case-sensitive keywords and cannot be used as variable names or identifiers in Python programs.

# Variables

- A variable is a named place in the memory where a programmer can store<br>
  data and leter retrieve the data using the variable "name"

- Programmers get to choose the name of the variables

- You can change the contents of a variable in a leer statement

```python
x = 12.2
y = 14
x = 100
```

# Python Variable Name Rules

Must start with a letter or underscore<br>
Must consist of letters, numbers, and underscores<br>
Case Sensitive

# assignment Statements

We assign a value to a variable using the assignment statement (=)

An assignment statement consists of an expression on the <br>
right-hand side and a variable to store the result

```python
x = 3.9*x*(1-x)
```

# Numeric Expressions

| Operator | Description              |
| -------- | ------------------------ |
| `+`      | Addition                 |
| `-`      | Subtraction              |
| `*`      | Multiplication           |
| `/`      | Division                 |
| `//`     | Floor Division           |
| `%`      | Modulus (Remainder)      |
| `**`     | Exponentiation           |
| `==`     | Equality                 |
| `!=`     | Inequality               |
| `<`      | Less than                |
| `>`      | Greater than             |
| `<=`     | Less than or equal to    |
| `>=`     | Greater than or equal to |

## Order of Evaluation

- When we string operators together<br>
  python mush know which one to do first
- This called "operator precedence"
- Which operator "takes precedence" over the others?

```python
x = 1 + 2 * 3 - 4 / 5 ** 6
```

## Operator Precedence

- Remember the rules top to bottom
- When writing code use parentheses
- When writhing code keep mathematical expression simple enough<br>
  that they are easy to understand
- Break long series of mathematical operations up to make them<br>
  more clear

| Operator                                                           | Order of Evaluation |
| ------------------------------------------------------------------ | ------------------- |
| Parentheses `()`                                                   | Innermost first     |
| Exponentiation `**`                                                | Left to Right       |
| Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%` | Left to Right       |
| Addition `+`, Subtraction `-`                                      | Left to Right       |

# What does "Type" Mean?

- In Python variables, literals, and<br>
  constants have a "type"
- Python knows the difference between <br>
  an integer number and a string
- For example "+" means "addition" if<br>
  something is a number and <br>
  "concatenate" if somethingis a string
  > concatenate = put together

## Several Types of Numbers

- Numbers have two main types
  - Integer are whole numbers:<br>
    -14, -2, 0, 1, 100, 401233
  - Floating point Number have<br>
    decimal parts: -2.5, 0.0, 98.6, 14.0
- There are other number types - they <br>
  are variations on float and integer

## Type Conventions

- When you put an integer and <br>
  floating point in an <br>
  expression, the integer is <br>
  implicitly converted to a float
- You can control this with the <br>
  built-in function int() and <br>
  float()

## User Input

- We can instruct python to <br>
  pause and read data from<br>
  the user using the input() <br>
  function
- The input() function<br>
  returns a string

```python
nam = input("Who are you?")
print("welcome", nam)
```

### Converting User Input

- If we want to read a number<br>
  from the user, we must<br>
  convert it from a string to a <br>
  number using a type <br>
  conversion function
- Latter we will deal with bad <br>
  input data

```python
# Convert elevator floors
inp = input("Europe flore? ")
usf = int(inp) + 1
print("US floor", usf)
```

# Comments in Python

- Anything after a # is ignored by python
- Why comment?
  - Describe what is going to happen in a swquence of code
  - Document who wrote the code or other ancillary information
  - Turn of a line of code - perhaps temporarily
