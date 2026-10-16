# Introduction

# 1 Say "Hello, World!" With Python

my_string = "Hello, World!"
print(my_string)

# 2 Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys


def check(n: int) -> str:
    if n % 2 != 0:
        return "Weird"
    elif 2 <= n <= 5:
        return "Not Weird"
    elif 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"
        
if __name__ == '__main__':
    n = int(input().strip())
    print(check(n))

# 3 Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"{a+b}")
    print(f"{a-b}")
    print(f"{a*b}")

# 4 Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# 5 Loops

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

# 6 Write a function

def is_leap(year):
    leap = False
    
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))

# 7 Print Function

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1, end="")

# Data types

# 8 List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [
        [i,j,k]
        for i in range(x+1)
        for j in range(y+1)
        for k in range(z+1)
        if i + j + k != n
    ]
    
    print(result)

# 9 Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    score = sorted(set(arr))
    
    print(score[-2])

# 10 Nested Lists

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    scores = sorted(set(score for name, score in students))
    
    second_lowest_score = scores[1]
    
    second_lowest_students = sorted(name for name, score in students if score == second_lowest_score)
    
    for name in second_lowest_students:
        print(name)

# 11 Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print(f"{average:.2f}")
    
# 12 Lists

if __name__ == '__main__':
    N = int(input())
    
    list = []
    
    for _ in range(N):
        command = input().split()
        action = command[0]
        
        if action == "insert":
            list.insert(int(command[1]), int(command[2]))
        elif action == "print":
            print(list)
        elif action == "remove":
            list.remove(int(command[1]))
        elif action == "append":
            list.append(int(command[1]))
        elif action == "sort":
            list.sort()
        elif action == "pop":
            list.pop()
        elif action == "reverse":
            list.reverse()

# 13 Tuples (Python 2)

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print(hash(tuple(integer_list)))

# Strings

# 14 sWAP cASE

def swap_case(s):
    new = []
    for char in s:
        if char.isupper():
            new.append(char.lower())
        elif char.islower():
            new.append(char.upper())
        else:
            new.append(char)
    return ''.join(new)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# 15 String Split and Join

def split_and_join(line):
    lines = line.split(" ")
    return "-".join(lines)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# 16 What's Your Name?

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# 17 Mutations

def mutate_string(string, position, character):
    word = list(string)
    word[position] = character
    return ''.join(word)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# 18 Find a string

def count_substring(string, sub_string):
    
    count = 0
    
    for i in range(0, len(string) - len(sub_string) + 1):
        
        word = []
        
        for j in range(len(sub_string)):
           word.append(string[i+j])
           
        if "".join(word) == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# 19 String Validators

if __name__ == '__main__':
    s = input()
    
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
  
# 20 Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# 21 Text Wrap

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# 22 Designer Door Mat

n, m = map(int, input().split())

pattern = ".|."

for i in range (1, n, 2):
    print((pattern * i).center(m, "-"))

print("WELCOME".center(m,"-"))

for i in range(n - 2, 0, -2):
    print((pattern * i).center(m, "-"))

# 23 String Formatting

def print_formatted(number):
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# 24 Alphabet Rangoli

import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []
   
    for i in range(size):
        s = "-".join(alphabet[i:size][::-1] + alphabet[i + 1:size])
        lines.append(s.center(4 * size - 3, "-"))
    
    result = "\n".join(lines[::-1] + lines[1:])
    print(result)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# 25 Capitalize!

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    new = []
    for i in range(len(s)):
        if i == 0:
            new.append(s[0].upper())
        elif s[i-1] == " ":
            new.append(s[i].upper())
        else:
            new.append(s[i])
    return "".join(new)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# 26 The Minion Game

def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    length = len(string)
    
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i
            
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

# 27 Merge the Tools!

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        subsegment = string[i:i + k]
        
        unique_chars = "".join(dict.fromkeys(subsegment))
        
        print(unique_chars)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# Sets

# 28 Introduction to Sets

def average(array):
    elements = set(array)
    return sum(elements) / len(elements)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# 29 No Idea!

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    array = list(map(int, input().split()))
    
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    
    happiness = 0
    for num in array:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1
            
    print(happiness)

# 30 Symmetric Difference

if __name__ == '__main__':

    m = int(input())
    set_a = set(map(int, input().split()))
    
    n = int(input())
    set_b = set(map(int, input().split()))
    
    sym_difference = set_a.symmetric_difference(set_b)
    
    # Sort and print each element on a new line
    for val in sorted(sym_difference):
        print(val)

# 31 Set .add()

if __name__ == '__main__':
    n = int(input())
    
    stamps = set()
    for _ in range(n):
        stamps.add(input().strip())
        
    print(len(stamps))

# 32 Set .discard(), .remove() & .pop()

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    num_commands = int(input())
        
    for _ in range(num_commands):
        cmd = input().split()
        method = cmd[0]
            
        if method == "pop":
            s.pop()
        elif method == "remove":
            s.remove(int(cmd[1]))
        elif method == "discard":
            s.discard(int(cmd[1]))
                
    print(sum(s))

# 33 Set .union() Operation

if __name__ == '__main__':
    n = int(input())
    english_subs = set(map(int, input().split()))
    
    m = int(input())
    french_subs = set(map(int, input().split()))

    total_subs = english_subs.union(french_subs)
    
    print(len(total_subs))

# 34 Set .intersection() Operation

if __name__ == '__main__':
    n = int(input())
    english_subs = set(map(int, input().split()))
    
    m = int(input())
    french_subs = set(map(int, input().split()))
    
    both_subs = english_subs.intersection(french_subs)
    
    print(len(both_subs))

# 35 Set .difference() Operation

if __name__ == '__main__':
    n = int(input())
    english_subs = set(map(int, input().split()))
    
    m = int(input())
    french_subs = set(map(int, input().split()))
    
    english_only = english_subs.difference(french_subs)

    print(len(english_only))

# 36 Set .symmetric_difference() Operation

if __name__ == '__main__':
    n = int(input())
    english_subs = set(map(int, input().split()))
    
    m = int(input())
    french_subs = set(map(int, input().split()))
    
    either_not_both = english_subs.symmetric_difference(french_subs)
    
    print(len(either_not_both))

# 37 Set Mutations

if __name__ == '__main__':
    len_a = int(input())
    set_a = set(map(int, input().split()))
    
    n = int(input())
    
    for _ in range(n):
        operation, _ = input().split()
        other_set = set(map(int, input().split()))
        
        getattr(set_a, operation)(other_set)
        
    print(sum(set_a))

# 38 The Captain's Room

if __name__ == '__main__':
    k = int(input())
    
    room_list = list(map(int, input().split()))
    
    unique_rooms = set(room_list)
    captain_room = (sum(unique_rooms) * k - sum(room_list)) // (k - 1)
    
    print(captain_room)

# 39 Check Subset

if __name__ == '__main__':
    num_test_cases = int(input())
    
    for _ in range(num_test_cases):
        len_a = int(input())
        set_a = set(map(int, input().split()))
        
        len_b = int(input())
        set_b = set(map(int, input().split()))
        
        print(set_a.issubset(set_b))

# 40 Check Strict Superset

if __name__ == '__main__':
    set_a = set(map(int, input().split()))
    
    n = int(input())
    
    is_strict_superset = True
    
    for _ in range(n):
        other_set = set(map(int, input().split()))
        
        if not set_a.issuperset(other_set) or set_a == other_set:
            is_strict_superset = False
            break
            
    print(is_strict_superset)

# Collections

# 41 Collections.Counter()

from collections import Counter

if __name__ == '__main__':
    num_shoes = int(input())
    
    inventory = Counter(map(int, input().split()))
    
    num_customers = int(input())
    
    total_earned = 0
    
    for _ in range(num_customers):
        size, price = map(int, input().split())
        
        if inventory[size] > 0:
            total_earned += price
            inventory[size] -= 1 
            
    print(total_earned)

# 42 DefaultDict Tutorial

from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    group_a = defaultdict(list)
    for i in range(1, n + 1):
        word = input().strip()
        group_a[word].append(str(i))
        
    for _ in range(m):
        word = input().strip()
        if word in group_a:
            print(" ".join(group_a[word]))
        else:
            print(-1)

# 43 Collections.namedtuple()

from collections import namedtuple

n, Student = int(input()), namedtuple('Student', input().split())
students = [Student(*input().split()) for _ in range(n)]
print(f"{sum(int(s.MARKS) for s in students) / n:.2f}")

# 44 Collections.OrderedDict()

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    item_dict = OrderedDict()
    
    for _ in range(n):
        item_name, net_price = input().rsplit(' ', 1)
        net_price = int(net_price)
        
        item_dict[item_name] = item_dict.get(item_name, 0) + net_price

    for item_name, total_price in item_dict.items():
        print(f"{item_name} {total_price}")

# 45 Word Order

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    word_counts = OrderedDict()
    
    for _ in range(n):
        word = input().strip()
        word_counts[word] = word_counts.get(word, 0) + 1
        
    print(len(word_counts))
    
    print(*(word_counts.values()))

# 46 Collections.deque()

from collections import deque

if __name__ == '__main__':
    n = int(input())
    d = deque()
    
    for _ in range(n):
        cmd = input().split()
        method = cmd[0]
        
        if len(cmd) > 1:
            getattr(d, method)(int(cmd[1]))
        else:
            getattr(d, method)()
            
    print(*(d))

# 47 Company Logo

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = input().strip()
    
    counts = Counter(s)

    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")


# 48 Piling Up!

from collections import deque

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        blocks = deque(map(int, input().split()))
        
        possible = True
        last_picked = float('inf') 
        
        while blocks:
            if blocks[0] >= blocks[-1]:
                current = blocks.popleft()
            else:
                current = blocks.pop()
                
            if current > last_picked:
                possible = False
                break
                
            last_picked = current
            
        if possible:
            print("Yes")
        else:
            print("No")

# 49 Calendar Module

import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split())
    
    day_index = calendar.weekday(year, month, day)
    
    day_name = calendar.day_name[day_index].upper()
    
    print(day_name)

# 50 Time Delta

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    date_format = "%a %d %b %Y %H:%M:%S %z"
    
    dt1 = datetime.strptime(t1, date_format)
    dt2 = datetime.strptime(t2, date_format)
    
    difference = abs(int((dt1 - dt2).total_seconds()))
    
    return str(difference)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

# 51 Exceptions

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        try:
            a, b = input().split()
            print(int(a) // int(b))
        except (ZeroDivisionError, ValueError) as e:
            print("Error Code:", e)

# 52 Zipped!

if __name__ == '__main__':
    n, x = map(int, input().split())
    
    marks = [list(map(float, input().split())) for _ in range(x)]
    
    for student_scores in zip(*marks):
        print(sum(student_scores) / x)


# 53 Athlete Sort

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    arr.sort(key=lambda x: x[k])

    for row in arr:
        print(*row)

# 54 ginortS

if __name__ == '__main__':
    s = input().strip()
    
    def sort_key(c):
        if c.islower():
            return (0, c)
        elif c.isupper():
            return (1, c)
        elif c.isdigit():
            if int(c) % 2 != 0:
                return (2, c)
            else:
                return (3, c)  

    
    print("".join(sorted(s, key=sort_key)))

# 55 Map and Lambda Function

cube = lambda x: x ** 3

def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))



# 56 XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    return len(node.attrib) + sum(get_attr_number(child) for child in node)

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

# 57 XML2 - Find the Maximum Depth

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth

    if level + 1 > maxdepth:
        maxdepth = level + 1
        
    for child in elem:
        depth(child, level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

# 58 Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        formatted_numbers = [f"+91 {num[-10:-5]} {num[-5:]}" for num in l]
        return f(formatted_numbers)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

# 59 Decorators 2 - Name Directory

import operator

def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
        
        return [f(person) for person in people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# 60 Arrays 

import numpy

def arrays(arr):
    return numpy.array(arr[::-1], float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# 61 Shape and Reshape

import numpy

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    
    matrix = numpy.array(arr).reshape(3, 3)
    
    print(matrix)

# 62 Transpose and Flatten

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    arr = numpy.array(matrix)
    
    print(numpy.transpose(arr))
    print(arr.flatten())

# 63 Concatenate

import numpy

if __name__ == '__main__':
    n, m, p = map(int, input().split())

    arr_1 = numpy.array([list(map(int, input().split())) for _ in range(n)])
    
    arr_2 = numpy.array([list(map(int, input().split())) for _ in range(m)])
    
    result = numpy.concatenate((arr_1, arr_2), axis=0)
    
    print(result)

# 64 Zeros and Ones

import numpy

if __name__ == '__main__':
    shape = tuple(map(int, input().split()))
    
    print(numpy.zeros(shape, dtype=int))
    
    print(numpy.ones(shape, dtype=int))

# 65 Eye and Identity

import numpy

numpy.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    print(numpy.eye(n, m))

# 66 Array Mathematics

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    a = numpy.array([list(map(int, input().split())) for _ in range(n)])
    b = numpy.array([list(map(int, input().split())) for _ in range(n)])
    
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(a ** b)

# 67 Floor, Ceil and Rint

import numpy

numpy.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    a = numpy.array(input().strip().split(), float)
    
    print(numpy.floor(a))
    print(numpy.ceil(a))
    print(numpy.rint(a))

# 68 Sum and Prod

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    arr = numpy.array([list(map(int, input().split())) for _ in range(n)])
    
    sum_axis_0 = numpy.sum(arr, axis=0)
    result = numpy.prod(sum_axis_0)
    
    print(result)

# 69 Min and Max

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    arr = numpy.array([list(map(int, input().split())) for _ in range(n)])
    
    min_axis_1 = numpy.min(arr, axis=1)
    result = numpy.max(min_axis_1)
    
    print(result)

# 70 Mean, Var, and Std

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    arr = numpy.array([list(map(int, input().split())) for _ in range(n)])

    print(numpy.mean(arr, axis=1))
    
    print(numpy.var(arr, axis=0))
    
    std_val = numpy.std(arr, axis=None)
    print(numpy.round(std_val, 11))

# 71 Dot and Cross

import numpy

if __name__ == '__main__':
    n = int(input())
    
    a = numpy.array([list(map(int, input().split())) for _ in range(n)])
    
    b = numpy.array([list(map(int, input().split())) for _ in range(n)])
    
    print(numpy.dot(a, b))

# 72 Inner and Outer

import numpy

if __name__ == '__main__':
    a = numpy.array(list(map(int, input().split())))
    b = numpy.array(list(map(int, input().split())))
    
    print(numpy.inner(a, b))
    
    print(numpy.outer(a, b))

# 73 Polynomials

import numpy

if __name__ == '__main__':
    coefficients = list(map(float, input().split()))
    
    x = float(input())
    
    print(numpy.polyval(coefficients, x))

# 74 Linear Algebra

import numpy

if __name__ == '__main__':
    n = int(input())

    a = numpy.array([list(map(float, input().split())) for _ in range(n)])
    
    det = numpy.linalg.det(a)
    print(round(det, 2))

# 75 Detect Floating Point Number

import re

if __name__ == '__main__':
    pattern = r'^[+-]?\d*\.\d+$'
    
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(bool(re.match(pattern, s)))


# 76 Re.split()

regex_pattern = r"[,.]"

import re
print("\n".join(re.split(regex_pattern, input())))

# 77 Group(), Groups() & Groupdict()

import re

if __name__ == '__main__':
    pattern = r'([a-zA-Z0-9])\1'
    
    match = re.search(pattern, input())

    print(match.group(1) if match else -1)

# 78 Re.findall() & Re.finditer()

import re

if __name__ == '__main__':
    s = input().strip()
    
    vowels = 'aeiouAEIOU'
    consonants = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
    
    pattern = rf'(?<=[{consonants}])([{vowels}]{{2,}})(?=[{consonants}])'
    
    matches = re.findall(pattern, s)
    
    if matches:
        for m in matches:
            print(m)
    else:
        print(-1)

# 79 Re.start() & Re.end()

import re

if __name__ == '__main__':
    s = input().strip()
    k = input().strip()
    
    pattern = rf'(?=({k}))'
    
    matches = list(re.finditer(pattern, s))
    
    if matches:
        for m in matches:
            start = m.start()
            end = start + len(k) - 1
            print((start, end))
    else:
        print((-1, -1))

# 80 Regex Substitution

import re

def change_operators(match):
    symbol = match.group(0)
    if symbol == "&&":
        return "and"
    elif symbol == "||":
        return "or"

if __name__ == '__main__':
    pattern = r'(?<= )(&&|\|\|)(?= )'
    
    n = int(input())
    for _ in range(n):
        line = input()
        print(re.sub(pattern, change_operators, line))

# 81 Validating Roman Numerals

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))

# 82 Validating phone numbers

import re

if __name__ == '__main__':
    pattern = r'^[789]\d{9}$'
    
    n = int(input())
    for _ in range(n):
        s = input().strip()
        if re.match(pattern, s):
            print("YES")
        else:
            print("NO")

# 83 Validating and Parsing Email Addresses

import email.utils
import re

if __name__ == '__main__':
    pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    
    n = int(input())
    for _ in range(n):
        line = input().strip()
        name, addr = email.utils.parseaddr(line)
        
        if re.match(pattern, addr):
            print(email.utils.formataddr((name, addr)))

# 84 Hex Color Code

import re

if __name__ == '__main__':
    pattern = r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b'
    
    n = int(input())
    inside_block = False
    
    for _ in range(n):
        line = input()

        if '{' in line:
            inside_block = True
            continue  
        elif '}' in line:
            inside_block = False
            
        if inside_block:
            matches = re.finditer(pattern, line)
            for m in matches:
                print(m.group(0))

# 85 HTML Parser - Part 1

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

if __name__ == '__main__':
    n = int(input())
    html_content = "".join(input() for _ in range(n))
    
    parser = MyHTMLParser()
    parser.feed(html_content)

# 86 HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)

if __name__ == '__main__':
    n = int(input())
    html_content = "\n".join(input() for _ in range(n))
    
    parser = MyHTMLParser()
    parser.feed(html_content)

# 87 Detect HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

if __name__ == '__main__':
    n = int(input())
    html_content = "\n".join(input() for _ in range(n))
    
    parser = MyHTMLParser()
    parser.feed(html_content)

# 88 Validating UID

import re

def is_valid_uid(uid):
    if len(uid) != 10:
        return False
    
    if not uid.isalnum():
        return False
    
    if len(set(uid)) != 10:
        return False
    
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False
    
    if len(re.findall(r'[0-9]', uid)) < 3:
        return False
    
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        uid = input().strip()
        print("Valid" if is_valid_uid(uid) else "Invalid")

# 89 Validating Credit Card Numbers

import re

def is_valid_credit_card(card):
    structure_pattern = r'^[456](\d{15}|\d{3}(-\d{4}){3})$'
    
    if not re.match(structure_pattern, card):
        return False
    
    raw_digits = card.replace('-', '')
    
    if re.search(r'(\d)\1{3,}', raw_digits):
        return False
    
    return True

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        card = input().strip()
        print("Valid" if is_valid_credit_card(card) else "Invalid")

# 90 Validating Postal Codes

regex_integer_in_range = r"^[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# 91 Matrix Script

#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

raw_script = "".join(matrix[row][col] for col in range(m) for row in range(n))
decoded_script = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', raw_script)

print(decoded_script)

# 92 Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_height = max(candles)
    counter = Counter(candles)
    return counter[max_height]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# 93 Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# 94 Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    shared = 5
    cumulative_likes = 0
    
    for _ in range(n):
        liked = shared // 2
        cumulative_likes += liked
        shared = liked * 3
        
    return cumulative_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# 95 Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    if len(n) == 1:
        return int(n)
    
    initial_sum = sum(int(digit) for digit in n)
    
    total_sum = initial_sum * k
    
    return superDigit(str(total_sum), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

# 96 Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    target = arr[-1]
    i = n - 2

    while i >= 0 and arr[i] > target:
        arr[i + 1] = arr[i]
        print(*(arr))
        i -= 1
        
    arr[i + 1] = target
    print(*(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# 97 Insertion Sort - Part 2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        target = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > target:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = target
        
        print(*(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
