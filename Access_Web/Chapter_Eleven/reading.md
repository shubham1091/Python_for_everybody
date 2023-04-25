# <span style="color:#f6fc2d">Regular Expressions</span>

In computing, a regular expression, also referred to as "regex" or "regexp", provides<br>
a concise and flexible means for matching strings of text, such as particular characters,<br>
words, or patterns of characters. A regular expression is written in a formal language<br>
that can be interpreted by a regular expression processor.

<a href="http://en.wikipedia.org/wiki/Regular_expression"> article on regular expression</a>

Really clever "wild card" expressions for matching and parsing strings

## <span style="color:#f6fc2d">Understanding Regular Expressions</span>

- Very powerful and quite cryptic
- Fun once you understand them
- Regular expressions are a language into themselves
- A language of "marker characters" - programming with characters
- It is kind of an "old school" language - compact

![Alt text](https://imgs.xkcd.com/comics/regular_expressions.png)

## <span style="color:#f6fc2d">Regular Expressions Quick Guide</span>

A collection of common regular expressions for pattern matching and text processing.

| Regular Expression | Description                                         |
| ------------------ | --------------------------------------------------- |
| `.`                | Match any character except a newline                |
| `^`                | Matches the beginning of a line                     |
| `$`                | Matches the end of a line                           |
| `\s`               | Matches whitespace                                  |
| `\S`               | Matches any non-whitespace character                |
| `*`                | Repeats a character zero or more times              |
| `*?`               | Repeats a character zero or more times (non-greedy) |
| `+`                | Repeats a character one or more times               |
| `+?`               | Repeats a character one or more times (non-greedy)  |
| `[aeiou]`          | Matches a single character in the listed set        |
| `[^XYZ]`           | Matches a single character not in the listed set    |
| `[a-z0-9]`         | The set of characters can include a range           |
| `(`                | Indicates where string extraction is to start       |
| `)`                | Indicates where string extraction is to end         |

## <span style="color:#f6fc2d">The Regular Expression Module</span>

- Before you can use regular expressions in you program, you <br>
  must import the library using "<span style="color: #94ed1f">import re</span>"
- You can use <span style="color: #94ed1f">re.search()</span> to see if a string matches a regular <br>
  expression, similar to using the <span style="color:#ae1fd1">find()</span> method for string
- You can use <span style="color: #94ed1f">re.findall()</span> to extract portions of a string that match <br>
  your regular expression, similar to a combination of <span style="color:#ae1fd1">find()</span> and<br>
  slicing: <span style="color:#ae1fd1">var[5:10]</span>

### <span style="color:#f6fc2d">Using</span><span style="color:#94ed1f"> re.search() </span><span style="color:#f6fc2d">Like</span><span style="color:#ae1fd1"> find()</span>

<table>
<tr>
    <th>without regular expression</th>
    <th>with regular expression</th>
</tr>
<tr>
<td>

```python
hand = open('mbox-short.txt', 'r')
for line in hand:
    line = line.rstrip()
    if line.find("From:") >=0:
        print(line)
```

</td>

<td>

```python
import re
hand = open('mbox-short.txt', 'r')
for line in hand:
    line = line.rstrip()
    if re.search("From:", line):
        print(line)
```

</td>
</tr>
</table>

### <span style="color:#f6fc2d">Using</span><span style="color:#94ed1f"> re.search() </span><span style="color:#f6fc2d">Like</span><span style="color:#ae1fd1"> startswith()</span>

<table>

<tr>
    <th>without regular expression</th>
    <th>with regular expression</th>
</tr>
<tr>
<td>

```python
hand = open('mbox-short.txt', 'r')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
```

</td>

<td>

```python
import re
hand = open('mbox-short.txt', 'r')
for line in hand:
    line = line.rstrip()
    if re.search("^From:", line):
        print(line)
```

</td>
</tr>
</table>

We fine-tune what is matched by adding special characters to the string

## <span style="color:#f6fc2d">Wild-Card Characters</span>

- The <span style="color:#94ed1f">dot</span> characters matches any character
- If you add the <span style="color:#ed971f">asterisk</span> character, the character is "any number of times"

| Line                                    | Regular Expression |
| --------------------------------------- | ------------------ |
| X-Sieve: CMU Sieve 2.3                  | ^X.\*:             |
| X-DSPAM-Result: Innocent                |                    |
| X-DSPAM-Confidence: 0.8475              |                    |
| X-Content-Type-Message-Body: text/plain |                    |

`^X.*:` &#8594; The regular expression `^X.*:` matches the beginning of a line (^), followed by the character "X" literally, followed by zero or more occurrences of any character (except newline) (.\*), and finally followed by a colon (:).

## <span style="color:#f6fc2d">Fine-Tuning Your Match</span>

Depending on how "clean" your data is and the purpose of your <br>
application, you may want to narrow your match down a bit

| Line                                  | Regular Expression |
| ------------------------------------- | ------------------ |
| X-Sieve: CMU Sieve 2.3                | ^X-\s+:            |
| X-DSPAM-Result: Innocent              |                    |
| X-DSPAM-Confidence: 0.8475            |                    |
| X-Plane is behind schedule: two weeks |                    |

`^X-\s+:` &#8594; The regular expression `^X-\s+:` matches the beginning of a line (^), followed by the characters "X-" literally, followed by one or more non-whitespace characters (\s+), and finally followed by a colon (:).

# <span style="color:#f6fc2d">Extracting Data</span>

## <span style="color:#f6fc2d">Matching and Extracting Data</span>

- re.search() returns a True/False depending on wether the <br>
  string matches the regular expression
- If we actually want the matching strings to be extracted, we <br>
  use re.findall()

```python
>>> import re
>>> x = "My 2 favorite numbers are 19 and 42"
>>> y = re.findall('[0-9]+',x)
>>> print(y)
['2','19','42']
```

`[0-9]+` &#8594; The regular expression `[0-9]+` matches one or more occurrences of any digit.

When we use re.findall(), it returns a list of zero or more sub-<br>
strings that match the regular expression

```python
>>> import re
>>> x = "My 2 favorite numbers are 19 nad 42"
>>> y = re.findall('[0-9]+',x)
>>> print(y)
['2','19','42']
>>> y = re.findall('[AEIOU]+',x)
>>> print(y)
[]
```

The regular expression `[AEIOU]+` matches one or more occurrences of any of the following uppercase vowels: A, E, I, O, or U.

## <span style="color:#f6fc2d">Warning:</span><span style="color:#ae1fd1"> Greedy </span><span style="color:#f6fc2d">Matching</span>

The repeat characters (\* and +) push <span style="color:#ae1fd1">outward</span> in both directions<br>
(greedy) to match the largest possible string

```python
>>> import re
>>> x = "From: Using the : character"
>>> y = re.findall('^F.+:', x)
>>> print(y)
['From: Using the :']
```

## <span style="color:#34ebd2">Non-Greedy </span><span style="color:#f6fc2d">Matching</span>

Not all regular expression repeat codes are greedy!<br>
If you add a ? character, the + and \* chill out a bit...

```python
>>> import re
>>> x = "From: Using the : character"
>>> y = re.findall('^F.+?:', x)
>>> print(y)
['From:']
```
