# <span style="color:#f6fc2d">Dictionaries</span>

## <span style="color:#f6fc2d">What is a Collection?</span>

- A collection is nice because we can put more than one value in it<br>
  and carry them all around in a convenient package
- We have a bunch of values in a single "variable"
- We do this by having more than one place "in" the variable
- We have ways of finding the different places in the variable

### <span style="color:#f6fc2d">What is Not A "Collection"?</span>

Most of our <span style="color: #94ed1f">variables</span> have one value in them - when we put a new <br>
value in the <span style="color: #94ed1f">variable</span>, the old value is overwritten

```python
$ python
>>> x = 2
>>> x = 4
>>> print(x)
4
```

### <span style="color:#f6fc2d">A Story of Two Collections...</span>

#### <span style="color:#94ed1f">List</span>

- A linear collection of values that stay in order

#### <span style="color:#ae1fd1">Dictionary</span>

- A "bag" of values, each with its own lable

## <span style="color:#f6fc2d">Dictionaries</span>

- Dictionaries are python's most powerful data collection
- Dictionaries allow us to do fast database-like operation in python
- Dictionaries have different names in different languages

  - Associative Arrays - perl / php
  - Properties or Map or HashMap - Java
  - Property Bag - c# / .Net

- List <span style="color:#34ebd2">index</span> their entries based on the position in the list
- <span style="color:#ae1fd1">Dictionary</span> are like a bag- no order
- So we <span style="color:#34ebd2">index</span> the things we put in the <span style="color:#ae1fd1">dictionary</span> with a "<span style="color:#34ebd2">lookup tag</span>"

```python
>>> purse = dict()
>>> purse['money'] = 12
>>> purse['candy'] = 3
>>> purse['tissues'] = 75
>>> print(purse)
{'money':12,'tissues':75,'candy':3}
>>> print(purse['candy'])
3
>>> purse['candy'] = purse['candy'] + 2
>>> print(purse)
{'money':12,'tissues':75,'candy':5}
```

## <span style="color:#f6fc2d">Comparing Lists and dictionaries</span>

<span style="color:#ae1fd1">Dictionary</span> are like <span style="color: #94ed1f">lists</span> except that they use <span style="color:#ed971f">keys</span> insted of numbers to look up <span style="color:#f6fc2d">values</span>

<table>
<tr>
<th>List</th>
<th>Dictionaries</th>
</tr>
<tr>
<td>

```python
>>> lst = list()
>>> lst.append(21)
>>> lst.append(183)
>>> print(lst)
[21, 183]
>>> lst[0] = 23
>>> print(lst)
[23, 183]
```

</td>
<td>

```python
>>> ddd = dict()
>>> ddd['age'] = 21
>>> ddd['course'] = 182
>>> print(ddd)
{'course':182,'age':21}
>>> ddd['age'] = 23
>>> print(ddd)
{'course':182,'age':23}

```

</td>
</tr>
</table>

# <span style="color:#f6fc2d">Counting with Dictionaries</span>

## <span style="color:#f6fc2d">Many Counters with a Dictionary</span>

One common use of dictionaries is <span style="color:#f6fc2d">counting</span> how often we "see" something

```python
>>> ccc = dict()
>>> ccc['csev'] = 1
>>> ccc['cwen'] = 1
>>> print(ccc)
{'csev': 1, 'cwen': 1}
>>> ccc['cwen'] = ccc['cwen'] +1
>>> print(ccc)
{'csev': 1, 'cwen':2}
```

### <span style="color:#f6fc2d">Dictionary Tracebacks</span>

- it is an <span style="color:#ae1fd1">error</span> to reference a key which is not in the dictionary
- We can use the <span style="color: #94ed1f">in</span> operator to see if a key is in the dictionary

```python
>>> ccc = dict()
>>> print(ccc['csev'])
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
KeyError: 'csev'
>>> 'csev' in ccc
False
```

## <span style="color:#f6fc2d">When We See a New Name</span>

When we encounter a new name, we need to add a new entry in the <br>
<span style="color:#ae1fd1">dictionary</span> and if this the second or leter time we have seen the <span style="color: #94ed1f">name</span>,<br>
we simply add one to the counter in the <span style="color:#ae1fd1">dictionary</span> undder that <span style="color: #94ed1f">name</span>

<table>
<tr>
<th>Code</th>
<th>Output</th>
</tr>
<tr>
<td>

```python
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
```

</td>
<td>

```python
{'csev': 2,'zqian':1,'cwen':2}

```

</td>
</tr>
</table>

### <span style="color:#f6fc2d">The </span><span style="color:#ae1fd1">get </span><span style="color:#f6fc2d">Method for Dictionaries</span>

The pattern of checking to see if a <span style="color:#34ebd2">key</span> is already in a dictionary and<br>
assuming a default value if the <span style="color:#34ebd2">key</span> is not there is so common that there<br>
is a <span style="color:#ae1fd1">method</span> colled <span style="color:#ae1fd1">get()</span> that does this for us<br>

<span style="color:#ed971f">Default value if key does not exist (and no Traceback).</span>

#### <span style="color:#f6fc2d">Simplified Counting with </span><span style="color:#ae1fd1">get() </span>

We can use <span style="color:#ae1fd1">get</span>() and provide a <span style="color:#ed971f">default value of zero</span> when the <span style="color:#34ebd2">key</span> <br>
is not yet in the dictionary - and then just add one

<table>
<tr>
<th>Code</th>
<th>Output</th>
</tr>
<tr>
<td>

```python
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
```

</td>
<td>

```python
{'csev': 2,'zqian':1,'cwen':2}

```

</td>
</tr>
</table>

# <span style="color:#f6fc2d">Dictionaries and Files</span>

## <span style="color:#f6fc2d">Definite Loops and Dictionaries</span>

Even though <span style="color: #94ed1f">dictionaries</span> are not stored in order, we can write a <span style="color:#f6fc2d">for</span><br>
loop that goes through all the <span style="color:#34ebd2">entries</span> in a <span style="color: #94ed1f">dictionaries</span> - actually it goes<br>
through all of the <span style="color:#34ebd2">keys</span> in the <span style="color: #94ed1f">dictionaries</span> and <span style="color:#34ebd2">looks up</span> the values

```python
>>> counts = {'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
>>> for key in counts:
...     print(key, counts[key])
...
jan 100
chuck 1
fred 42
>>>
```

### <span style="color:#f6fc2d">Retrieving lists of Keys and Values</span>

You can get a list of <span style="color: #94ed1f">keys</span>, <span style="color:#ae1fd1">values</span>, or <span style="color:#ed971f">items(both)</span> from a dictionary

```python
>>> jjj = {'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
>>> print(list(jjj))
['jan', 'chuck', 'fred']
>>> print(jjj.keys())
['jan', 'chuck', 'fred']
>>> print(jjj.values())
[100, 1, 42]
>>> print(jjj.items())
[('jan', 100), ('chuck', 1), ('fred', 42)]
>>>
```

# <span style="color:#f6fc2d">Bonus: Two Iteration Variables!</span>

- We loop through the <span style="color:#ed971f">key</span> - <span style="color:#f6fc2d">value</span> pairs in a dictionary using \*two\* iteration variables
- Each iteration, the first variable is the <span style="color:#ed971f">key</span> and the second variable is the corresponding <span style="color:#f6fc2d">value</span> for the key

<table>
<tr>
<th>Code</th>
<th>Output</th>
</tr>
<tr>
<td>

```python
jjj = {'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
for k, v in jjj.items():
    print(k, v)
```

</td>
<td>

```python
jan 100
chuck 1
fred 42
```

</td>
</tr>
</table>
