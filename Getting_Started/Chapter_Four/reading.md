# <span style="color:#f6fc2d"> Stored (and reused) Steps</span>

## Building our Own Functions

- We createa new function using the def keyword followed by optional<br>
  parameters in parentheses
- We indent the body of the function
- This <span style="color:#f6fc2d">defines </span> the function but <span style="color:#ed971f">does not</span> execute the body of the function

<table>
<tr>
<th>code</th>
<th>output</th>
</tr>
<tr>
<td>

```python
x = 5
print("Hello")
#define the function
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work alll day.")
print("Yo")
# the function never got colled
x = x + 2
print(x)
```

</td>
<td>

```
Hello
Yo
7
```

</td>
</tr>
<tr>
<td>

```python
x = 5
print("Hello")
#define the function
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work alll day.")
print("Yo")
#invoking the function
print_lyrics()
x = x + 2
print(x)
```

</td>
<td>

```
Hello
Yo
I'm a lumberjack, and I'm okay.
I sleep all night and I work alll day.
7
```

</td>
</tr>

</table>

## Parameters

A <span style="color:#34ebd2"> Parameter</span> is a variable which we use <span style="color:#ae1fd1"> in</span> the function <span style="color:#f6fc2d">definition</span>. <br>
It is a "handle" that allows the code in the function to access the <br>
<span style="color:#ed971f">argument</span> for a particular function invocation.

```python
>>> def greet(lang):
        if lang == "es":
            print("Hola")
        elif lang == "fr":
            print("Bonjour")
        else:
            print("Hello")
>>> greet("en")
Hello
>>> greet("es")
Hola
>>> greet("fr")
Bonjour
```
### Multiple <span style="color:#34ebd2"> Parameter</span> /<span style="color:#ed971f"> Arguments</span>
- We can define more than one <span style="color:#34ebd2"> Parameter</span> in the <span style="color: #94ed1f"> function </span> definition
- We simply add more <span style="color:#ed971f"> arguments</span> when we call the <span style="color: #94ed1f"> function </span>
- We match the number and order of arguments and parameters
<table>
<tr>
<td>

```python
def addTwo(a,b):
    c = a + b
    print("Total is",c)
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
addTwo(num1, num2)
```
</td>
<td>

```
Enter number: 10
Enter number: 50
Total is 60
```
</td>
</tr>
</table>

## <span style="color:#">Return Values</span>

Often a function will take its arguments, do some computation, and<br>
<span style="color:#ed971f">retrun</span> a value to be used as the value of the function call in the <br>
<span style="color:#ae1fd1">calling expression</span>. The <span style="color:#ed971f">return</span> keyword is used for this.

- A "fruitful" <span style="color: #94ed1f"> function </span>is one that produces a <span style="color:#ae1fd1"> result</span> (or <span style="color:#f6fc2d">return</span> <span style="color:#ae1fd1">value</span>)
- The <span style="color:#f6fc2d">return</span> statement ends the <span style="color: #94ed1f"> function </span> execution and "sends back" the<br>
  <span style="color:#ae1fd1">result</span> of the <span style="color: #94ed1f"> function </span>

```python
>>> def greet(lang):
        if lang == "es":
            print("Hola")
        elif lang == "fr":
            print("Bonjour")
        else:
            print("Hello")
>>> print(greet("en"),"Glenn")
Hello Glenn
>>> print(greet("es"),"Sally")
Hola Sally
>>> print(greet("fr"),"Michael")
Bonjour Michael

```
