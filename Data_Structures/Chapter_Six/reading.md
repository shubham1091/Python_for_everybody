# <span style="color:#f6fc2d">String data Type</span>

- <span style="color:#ae1fd1">A string is a sequence of characters</span>
- <span style="color:#ae1fd1">A string literal uses quotes<br>
  'Hello' or "Hello"</span>
- <span style="color: #94ed1f">For strings, + means "concatenate"</span>
- <span style="color:#ed971f">When a string contains numbers, it is<br>
  still a string</span>
- <span style="color:#34ebd2">We can convert numbers in a string into<br>
  a number using</span> <span style="color:#ae1fd1">int</span><span style="color:#34ebd2">()</span>

```python
>>> str1 = "Hello"
>>> str2 = 'there'
>>> bob = str1 + str2
>>> print(bob)
Hellothere
>>> str3 = '123'
>>> str4 = str3 + 1
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str'
and 'int' objects
>>> x = int(str3) + 1
>>> print(x)
124
>>>
```

## <span style="color:#f6fc2d">Reading and Converting</span>

- We prefer to read data in using <br>
  <span style="color:#ed971f">string</span> and then parse and convert<br>
  the data as we need
- This gives us more control over <br>
  error situation and/or bad user input
- Input numbers must be <span style="color:#ae1fd1">converted</span> from<br>
  strings

# <span style="color:#f6fc2d">Looking Inside Strings</span>

- We can get at any single character in a<br>
  string using an index specified in <span style="color:#34ebd2">square brackets</span>
- The index value must be an integer<br>
  and start at zero
- The index value can be an expression<br>
  that is computed

| b   | a   | n   | a   | n   | a   |
| --- | --- | --- | --- | --- | --- |
| 0   | 1   | 2   | 3   | 4   | 5   |

```python
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> x = 3
>>> w = fruit[x - 1]
>>> print(w)
n
```

## <span style="color:#f6fc2d">A Character Too Far</span>

- You will get a <span style="color:#b5473f">python error</span><br>
  if you attempt to index <br>
  beyond the end of a string
- So be careful when <br>
  constructing index values<br>
  and slices

```python
>>> zot = 'abc'
>>> print(zot[5])
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>>
```

### <span style="color:#f6fc2d">Strings Have Length</span>

The built-in function <span style="color:#ae1fd1">len</span> gives us <br>
the length of a string

| b   | a   | n   | a   | n   | a   |
| --- | --- | --- | --- | --- | --- |
| 0   | 1   | 2   | 3   | 4   | 5   |

```python
>>> fruit = 'banana'
>>> print(len(fruit))
6
```

## <span style="color:#f6fc2d">Looping Through Strings</span>

Using a <span style="color:#f6fc2d">while</span> statement and an <span style="color: #94ed1f">iteration variable</span>,<br>
and the <span style="color:#ae1fd1">len</span> function, we can construct a loop to <br>
look at each of the letters in a string individually<br>

<table>
<tr>
<th>Code</th>
<th>Output</th>
</tr>
<tr>
<td>

```python
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
```

</td>
<td>

```
0 b
1 a
2 n
3 a
4 n
5 a
```

</td>
</tr>
</table>

- A definite loop using a <span style="color:#f6fc2d">for</span> statement is much<br>
  more elegant
- The <span style="color: #94ed1f">iteration variable</span> is completely taken care<br>
  of by the <span style="color:#f6fc2d">for</span> loop

<table>
<tr>
<th>Code</th>
<th>Output</th>
</tr>
<tr>
<td>

```python
fruit = 'banana'
for letter in fruit:
    print(letter)
```

</td>
<td>

```
b
a
n
a
n
a
```

</td>
</tr>
</table>

## <span style="color:#f6fc2d">Slicing Strings</span>

- We can also look at any continuous section<br>
  of a string using a <span style="color:#34ebd2">colon operator</span>
- The second number is one beyond the end <br>
  of the slice-"up to but not including"
- If the second number is beyond the end <br>
  of the string, it stops at the end
- If we leave off the first number or the last<br>
  number of the slice, it is assumed to be the <br>
  beginning or end of the string respectively

| M   | o   | n   | t   | y   |     | P   | y   | t   | h   | o   | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  |

```python
>>> s = "Monty Python"
>>> print(s[0 : 4])
Mont
>>> print(s[6 : 7])
P
>>> print(s[6 : 20])
Python
>>> print(s[: 2])
Mo
>>> print(s[8 :])
thon
>>> print(s[:])
Monty Python
```

# <span style="color:#f6fc2d">Manipulating Strings</span>

## <span style="color:#f6fc2d">String Concatenation</span>

When the <span style="color:#34ebd2">+</span> operator is applied to string, it means <span style="color:#34ebd2">"concatenation"</span>

```python
>>> a = "Hello"
>>> b = a + "There"
>>> print(b)
HelloThere
>>> c = a + " " +"There"
>>> print(c)
Hello There
>>>
```

## Using <span style="color:#f6fc2d">in</span> as a Logical Operator

- The <span style="color:#f6fc2d">in</span> keyword can also be used to check if one<br>
  string is "in" another string
- The <span style="color:#f6fc2d">in</span> expression is a logical expression that<br>
  returns <span style="color:#ed971f">True</span> or <span style="color:#ed971f">False</span> and can be used in and <span style="color:#f6fc2d">if</span> statement

```python
>>> fruit = "banana"
>>> 'n' in fruit
True
>>> 'm' in fruit
False
>>> 'nan' in fruit
True
>>> if 'a' in fruit:
...     print("Found it!")
...
>>> Found it!
>>>
```

## <span style="color:#f6fc2d">String Comparison</span>

```python
if word == 'banana':
    print("All right, bananas.")
if word < "banana":
    print("Your word, "+ word + " comes before banana.")
elif word > "banana":
    print("Your word, "+ word + " comes after banana.")
else:
    print("All right, bananas.")
```

## <span style="color:#f6fc2d">String Library</span>

- Python has a number of string <span style="color:#ae1fd1">functions</span> which <br>
  are in the <span style="color:#ae1fd1">string library</span>y
- These <span style="color:#ae1fd1">functions</span> are already <span style="color:#ae1fd1">built into</span> every <br>
  string - we invoke them by appending the function<br>
  to the string variable
- These <span style="color:#ae1fd1">functions</span> do not modify the original string<br>
  instead they return a new string that has beed altered

```python
>>> greet = "Hello Bob"
>>> zap = greet.lower()
>>> print(zap)
hello bob
>>> print(greet)
Hello Bob
>>> print("Hi There".lower())
hi there
>>>
```

```python
>>> stuff = "Hello world"
>>> type(stuff)
<class 'str'>
# All the methods that are in str class
>>> dir(stuff)
['add', 'class', 'contains', 'delattr', 'dir', 'doc', 'eq', 'format', 'ge', 'getattribute',
'getitem', 'getnewargs', 'getstate', 'gt', 'hash', 'init', 'init_subclass', 'iter', 'le', 'len',
'lt', 'mod', 'mul', 'ne', 'new', 'reduce', 'reduce_ex', 'repr', 'rmod', 'rmul',
'setattr', 'sizeof', 'str', 'subclasshook', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

### <span style="color:#f6fc2d">Searching a String</span>

- We use the <span style="color:#ae1fd1">find()</span> function to search for a substring <br>
  within another string
- <span style="color:#ae1fd1">find()</span> finds the first occurrence ot the substring
- If the substring is not found, <span style="color:#ae1fd1">find()</span> returns -1
- <span style="color:#f6fc2d">Remember that string position starts at zero</span>

| b   | a   | n   | a   | n   | a   |
| --- | --- | --- | --- | --- | --- |
| 0   | 1   | 2   | 3   | 4   | 5   |

```python
>>> fruit = "banana"
>>> pos = fruit.find("na")
>>> print(pos)
2
>>> aa = fruit.find("z")
>>> print(aa)
-1
```

### <span style="color:#f6fc2d">Search and Replace</span>

- The <span style="color:#ae1fd1">replace()</span> function is like a "search and replace" <br>
  operation in a word processor
- It replaces <span style="color:#ed971f">all occurrences</span> of the <span style="color:#94ed1f">search string</span><br>
  with the <span style="color:#34ebd2">replacement string</span>

```python
>>> greet = "Hello Bob"
>>> nstr = greet.replace("Bob","Jane")
>>> print(nstr)
Hello Jane
>>> nstr = greet.replace("o","x")
>>> print(nstr)
Hellx Bxb
```

### <span style="color:#f6fc2d">Stripping Whitespace</span>

- Sometimes we want to take a string and remove<br>
  whitespace at the beginning and/or end
- <span style="color:#ae1fd1">lstrip()</span> and <span style="color:#ae1fd1">rstrip()</span> remove whitespace at <br>
  the left or right
- <span style="color:#ae1fd1">strip()</span> remove both beginning and ending whitespaces

```python
>>> greet = "     Hello Bob    "
>>> greet.lstrip()
'Hello Bob    '
>>> greet.rstrip()
'    Hello Bob'
>>> greet.strip()
'Hello Bob'
```

### <span style="color:#f6fc2d">Prefixes</span>

```python
>>> line = "Please have a nice day"
>>> line.startswith("Please")
True
>>> line.startswith("p")
False
```

## <span style="color:#f6fc2d">Parsing and Extracting</span>

```python
>>> data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
>>> atpos = data.find("@")
>>> print(atpos)
21
>>> sppos = data.find(" ", atpos)
>>> print(sppos)
31
>>> host = data[atpos + 1 : sppos]
>>> print(host)
uct.ac.za
```
