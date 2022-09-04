# Find Uppercase Letter in String

# find the first occurence of first uppercase letter

from cmath import e


str_1 = "lucidProgramming"
str_2 = "LucidProgramming"
str_3 = "lucidprogramming"

def find_uppercase_iter(s):
    for i in range(len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            return i
    return None

def find_uppercase_recusive(s):
    index = 0
    def _find(s,index):
        if index < len(s): 
            if s[index].isupper():
                return s[index]
            else:
                return _find(s , index + 1)
        else:
            return None
    return _find(s,index)

print("\nFirst capital letter in {} is = {}".format(str_1,find_uppercase_recusive(str_1)))
print("First capital letter in {} is = {}".format(str_2,find_uppercase_recusive(str_2))) 
print("First capital letter in {} is = {}\n".format(str_3,find_uppercase_recusive(str_3)))

# Calculate String Length
# calculate the length of a string using both an iterative and recursive approach in Python.


# Recursive length calculation: O(n)

def len_string_recursive(s):
    
    if s == "":
        return 0 
    return 1 + len_string_recursive(s[1:]) 
print(len_string_recursive(str_1))

# Count Consonants in String

def count_constant(s):
    if s == '':
        return 0
    elif s[0] !='a' or s[0] !='e' or s[0] !='o' or s[0] !='i' or s[0] !='o' or s[0] !='A' or s[0] !='E' or s[0] !='O' or s[0] !='I' or s[0] !='U':
        return 1 + count_constant(s[1:])
    else:
        return 0 + count_constant(s[1:])
    
print(count_constant("Welcome to Educative!"))