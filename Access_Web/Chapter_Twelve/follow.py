""" 
Following Links in Python

In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The 
program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat 
the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and 
the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. 
The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah

Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Troy.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. 
The answer is the last name that you retrieve.
"""

import urllib.request
from bs4 import BeautifulSoup

def get_last_name(url, position, repeats):
    """
    Retrieves the last name from a sequence of HTML pages.

    Args:
        url (str): The URL of the initial HTML page.
        position (int): The position of the link to follow relative to the first name.
        repeats (int): The number of times to repeat the process.

    Returns:
        str: The last name found after following the links.

    """
    print("Retrieving:", url)
    for i in range(repeats):
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        url = tags[position - 1].get('href', None)  # Get the URL from the link at the specified position
        print("Retrieving:", url)

    last_name = tags[position - 1].contents[0].strip()  # Get the contents of the link at the specified position as the last name
    return last_name

# Prompt for user input
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

# Call the function and display the last name found
last_name = get_last_name(url, position, count)
print("Last name found:", last_name)
