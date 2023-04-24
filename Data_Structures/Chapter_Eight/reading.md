# <span style="color:#f6fc2d">Lists</span>

## <span style="color:#f6fc2d">Programming</span>

### <span style="color:#ed971f">Algorithms</span>

- A set of rules or steps used to solve a problem

### <span style="color:#ed971f">Data Structures</span>

- A particular way of organizing data in a computer

## <span style="color:#f6fc2d">What is Not A "Collection"?</span>

Most of our <span style="color: #94ed1f">variables</span> have one value in them - when we put a new <br>
value in the <span style="color: #94ed1f">variable</span>, the old value is overwritten

```python
$ python
>>> x = 2
>>> x = 4
>>> print(x)
4
```

## <span style="color:#f6fc2d">A List Is a Kind of Collection</span>

- A <span style="color:#ae1fd1">Collection</span> allows us to put many values in a single "<span style="color: #94ed1f">variable</span>"
- A <span style="color:#ae1fd1">Collection</span> is nice because we can carry <span style="color:#ed971f">many values</span><br>
  around in one convenient package.

```python
friends = ['Joseph','Glenn','Sally']
carryon = ['socks', 'shirt', 'perfume']
```

## <span style="color:#f6fc2d">List Constants</span>

- <span style="color:#ed971f">List</span> constants are surrounded by square brackets and the<br>
  elements in the list are separated by commas
- A <span style="color:#ed971f">list</span> element can be any Python object- even <span style="color:#34ebd2">another list</span>
- A <span style="color:#ed971f">list</span> can be empty

```python
>>> print([1,24,76])
[1, 24, 76]
>>> print(['red', 'yellow', 'blue'])
['red', 'yellow', 'blue']
>>> print(['red', 24, 98.6])
['red', 24, 98.6]
>>> print([1,[5,6],7])
[1,[5, 6],7]
```

### <span style="color:#f6fc2d">We Already Use Lists!</span>

<table>
<tr>
<th>Code</th>
<th>Output</th>
</tr>
<tr>
<td>

```python
for i in [5,4,3,2,1]:
    print(i)
print("Blastoff!")
```

</td>
<td>

```
5
4
3
2
1
Blastoff!
```

</td>
</tr>
</table>

#### <span style="color:#f6fc2d">Lists and Definite Loops - Best Pals</span>

<table>
<tr>
<th>Code</th>
<th>Output</th>
</tr>
<tr>
<td>

```python
friends = ['Joseph','Glenn','Sally']
for friend in friends:
    print("Happy New Year:",friend)
print("Done!")
```

</td>
<td>

```
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
Done!
```

</td>
</tr>
</table>

### <span style="color:#f6fc2d">Looking Inside Lists</span>

Just like strings, we can get at any single element<br>
in a list using an index specified in <span style="color:#34ebd2">square brackets</span>

| Joseph | Glenn | Sally |
| ------ | ----- | ----- |
| 0      | 1     | 2     |

```python
>>> friends = ['Joseph','Glenn','Sally']
>>> print(friends[1])
Glenn
>>>
```

## <span style="color:#f6fc2d">Lists Are Mutable</span>

- Strings are "<span style="color: #94ed1f">immutable</span>" - we cannot change the contents of a <br>
  string - we must make a <span style="color:#ae1fd1">new string</span> to make any change
- Lists are "<span style="color: #94ed1f">mutable</span>" - we cannot <span style="color:#ae1fd1">change</span> an element of a list using<br>
  the <span style="color:#34ebd2">index</span> operator

```python
>>> fruit = 'Banana'
>>> fruit[0] = 'b'
Traceback
TypeError: 'str' object does not
support item assignment
>>> x = fruit.lower()
>>> print(x)
banana
>>> lotto = [2,14, 26,41,63]
>>> print(lotto)
[2,14,26,41,63]
>>> lotto[2] = 28
>>> print(lotto)
[2,14,28,41,63]
```

## <span style="color:#f6fc2d">How Long is a List?</span>

- The <span style="color:#ae1fd1">len()</span> function takes a <span style="color:#ed971f">list</span> as a parameter and returns the number<br>
  of <span style="color:#34ebd2">elements</span> in the <span style="color:#ed971f">list</span>
- Actually <span style="color:#ae1fd1">len()</span> tells us the number of elements of any set or sequence<br>
  (such as a string...)

```python
>>> greet = "Hello Bob"
>>> print(len(greet))
9
>>> x = [1,2,'joe',99]
>>> print(len(x))
4
```

## <span style="color:#f6fc2d">Using the </span><span style="color:#ae1fd1">Range</span><span style="color:#f6fc2d">Function</span>

- The <span style="color:#ae1fd1">range</span> function <span style="color:#ae1fd1">returns a list of numbers</span> that range<br>
  from zero to one less than the <span style="color:#34ebd2">parameter</span>
- We can construct an index loop using <span style="color:#f6fc2d">for</span> and and integer <span style="color: #94ed1f">iterator</span>

```python
>>> print(range(4))
[0, 1,2,3]
>>> friends = ['joseph', 'Glenn', 'Sally']
>>> print(len(friends))
3
>>> print(range(len(friends)))
[0,1,2]
```

# <span style="color:#f6fc2d">Manipulating Lists</span>

## <span style="color:#34ebd2">Concatenating </span><span style="color:#f6fc2d">Lists Using </span><span style="color:#34ebd2">+</span>

We can create a new list by adding two existing lists together

```python
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]
>>> print(a)
[1,2,3]
```

## <span style="color:#f6fc2d">Lists Can Be </span><span style="color:#34ebd2">Sliced</span><span style="color:#f6fc2d"> Using </span><span style="color:#34ebd2">:</span>

<span style="color: #94ed1f">Remember</span>: Just like in strings, the second number is "<span style="color:#ae1fd1">up to but not including</span>"

```python
>>> t = [9,41,12,3,74,15]
>>> t[1:3]
[41,12]
>>> t[:4]
[9,41,12,3]
>>> t[3:]
[3,74,15]
>>> t[:]
[9,41,12,3,74,15]
```

## <span style="color:#f6fc2d">Building a List from Scratch</span>

- We can create a empty <span style="color: #94ed1f">list</span> and then add elements using <br>
  the <span style="color:#ae1fd1">append</span> method
- The <span style="color: #94ed1f">list</span> stays in order and new elements are <span style="color:#ae1fd1">added</span> at<br>
  the end of the <span style="color: #94ed1f">list</span>

```python
>>> stuff = list()
>>> stuff.append('book')
>>> stuff.append(99)
>>> print(stuff)
['book', 99]
>>> stuff.append('cookie')
>>> print(stuff)
['book', 99, 'cookie']
```

## <span style="color:#f6fc2d">Is Something in a List?</span>

- Python provides two <span style="color:#f6fc2d">operators</span> that let you check if an item<br>
  is in a list
- These are logical operators that return <span style="color:#ae1fd1">True</span> or <span style="color:#ae1fd1">False</span>
- They do not modify the list

```python
>>> some = [1, 9, 21, 10, 16]
>> 9 in some
True
>>> 15 in some
False
>>> 20 not in some
True
```

## <span style="color:#f6fc2d">Lists are in Order</span>

- A <span style="color:#ed971f">list</span> can hold many items and keeps those items in the <br>
  order until we do somthing to change the order
- A <span style="color:#ed971f">list</span> can be <span style="color:#ae1fd1">sorted</span> (i.e., change its order)
- The <span style="color:#ae1fd1">sort</span> method (unlike in strings) means "<span style="color:#ae1fd1">sort yourself</span>"

```python
>>> friends = ['joseph', 'Glenn', 'Sally']
>>> friends.sort()
>>> print(friends)
['Glenn', 'Joseph', 'Sally']
>>> print(friends[1])
Joseph
```
