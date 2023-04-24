# <span style="color:#f6fc2d">Tuples</span>

## <span style="color:#f6fc2d">Tuples Are Like Lists</span>

Tuples are another kind of sequence that functions much like a list<br>
they have elements which are indexed starting at 0

```python
>>> x = ('Glenn', 'Sally', 'Joseph')
>>> print(x[2])
Joseph
>>> y = (1, 9, 2)
>>> print(y)
(1, 9, 2)
>>> print(max(y))
9
>>> for iter in y:
...     print(iter)
...
1
9
2
>>>
```

## <span style="color:#f6fc2d">but... Tuples are "immutable"</span>

Unlike a list, once you create a tuple, you cannot alter its<br>
contents - similar to a string

<table>
<tr>
<th>
List
</th>
<th>
String
</th>
<th>
Tuple
</th>
</tr>
<tr>
<td>

```python
>>> x = [9, 8, 7]
>>> x[2] = 6
>>> print(x)
[9, 8, 6]
```

</td>
<td>

```python
>>> y = 'ABX'
>>> y[2] = 'D'
Traceback: 'str' object does
not support item Assignment
>>>
```

</td>
<td>

```python
>>> z = (5, 4, 3)
>>> z[2] = 0
Traceback: 'tuple' object does
not support item Assignment
>>>
```

</td>
</tr>
</table>

## <span style="color:#f6fc2d">Tuples Are More Efficient</span>

- Since Python does not have to build tuple structures to be<br>
  modifiable, they are simpler and more efficient in terms of <br>
  memory use and performance than list
- So in our program when we are makin "temporary variables"<br>
  we prefer tuples over lists

## <span style="color:#f6fc2d">Tuples and Assignment</span>

- We can also put a tuple on the left-hand side of an assignment statement
- we can even omit the parentheses

```python
>>> (x, y) = (4, 'fred')
>>> print(y)
fred
>>> (a,b) = (99, 98)
>>> print(a)
99
```

## <span style="color:#f6fc2d">Tuples and Dictionaries</span>

The items() method in dictionaries returns a list of (key, value) tuples

```python
>>> d = dict()
>>> d['csev'] = 2
>>> d['cwen'] = 4
>>> for k, v in d.items():
...     print(k, v)
...
csev 2
cwen 4
>>> tups = d.items()
>>> print(tups)
dict_items([('csev', 2), ('cwen',4)])
```

## <span style="color:#f6fc2d">Tuples are Comparable</span>

The comparison operators work with tuples and other <br>
sequences. If the first item is equal, Python goes on to the next<br>
element, and so on, untile it finds elements that differ.

## <span style="color:#f6fc2d">Sorting List of Tuples</span>

- We can take advantage of the ability to sort a list of tuples to get a<br>
  sorted version of a dictionary
- First we sort the dictionary by the key using the items() method and <br>
  sorted() function

```python
>>> d = {'a':10, 'b': 1, 'c':22}
>>> d.items()
dict_items([('a',10),('c',22),('b',1])
>>> sorted(d.items())
[('a',10),('b',1),('c',22)]
```

## <span style="color:#f6fc2d">Sorting by Values Instead of Key</span>

- If we could construct alist of tuples of the from (value, key) <br>
  we could sort by value
- We do this with a for loop that creates a list of tuples

```python
>>> c = {'a':10,'b':1,'c':22}
>>> tmp = list()
>>> for k, v in c.items():
...     temp.append((v,k))
...
>>> print(tmp)
[(10,'a'),(22,'c'),(1,'b')]
>>> tmp = sorted(tmp,reverse=True)
>>> print(tmp)
[(22, 'c'),(10,'a'),(1,'b')]
```
