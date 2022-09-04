# look and say sequence
# my apporach is to have a stack and queue 
# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ... 

#
from functools import reduce

from numpy import str_


class myStack():
    
    def __init__(self) -> None:
        self.items = list()
    
    def peek(self):
        return self.items[-1]
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def __len__(self):
        return len(self.items)
    
    def is_empty(self):
        if self.items == list():
            return True 
        else:
            return False
           
def next_number_1(num):
    stack_1 = myStack()
    stack_2 = myStack()
    counter = 1    

    while num != 0:
        n = num  % 10
        num = num // 10
        stack_1.push(n)
    
    n = stack_1.pop()
    while not stack_1.is_empty():
        
        n2 = stack_1.pop()
        if n == n2:
            counter +=1
        else:
            stack_2.push(counter)
            stack_2.push(n)
            counter = 1
            n = n2           
    stack_2.push(counter)
    stack_2.push(n)
    
    a = reduce(lambda i,j: str(i) + str(j),stack_2.items)
       
    return a

def next_number_2(s):
    if type(s) != str():
        s = str(s) 
    
    size = len(s)
    index = 0
    counter = 1
    res = ''
    
    while index < size:
        
        if index  == size -1:  #last index so there is nothing to camper to
            res = res+str(counter)+s[index]
            index+=1 
        else:             
            if s[index] == s[index+1]:  # camper to next charecter if equal increase count by 1
                counter+=1
                index+=1
            else:
                res = res+str(counter) + s[index] # since the charcters are not equal so update the string and assign the counter to default value 1
                counter = 1
                index+=1
    return res   
     
def next_number_3(s):
    if type(s) != str():
        s = str(s)
    count = 1
    res = []
    i = 0
    while i < len(s):
        while i+1 < len(s) and s[i] == s[i+1]:
            count+=1
            i+=1
        res.append(str(count))
        res.append(s[i])
        count = 1
        i +=1
    return ''.join(res)

s = 1
for _ in range(4):
    print(s)
    s = next_number_3(s)
  
def column_to_id(s_id)->int:
    
    col_id = list(s_id)
    
    size = len(col_id)
    n = size
    res = 0
    for i in range(size):
        if col_id[i].isalpha() and col_id[i].isupper():
            Id_to_int = ord(col_id[i]) - ord('A') + 1
            n = n-1   #n which is exponant must be n = len(s) - 1
            res += pow(26,n) * Id_to_int
            
    return res
            
    
print(column_to_id("ZZ"))

# determine if the given string is palindrome
def is_palindrome(s)->bool:

    s = s.replace(" ","").lower()

    size = len(s) //2
    i = 0
    while i <= size:
        a = s[i]
        b =s[-i-1]
        if s[i] != s[-i-1]:
            return False
        i +=1
        
    return True
print(is_palindrome("was it a cat I saw"))


# we will determine whether two strings are anagrams of each other.
# Simply put, an anagram is when two strings can be written using the same letters.
def is_angram(s1,s2)->bool:
    
    #Normalizing the strings
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ","").lower()
    s1_dict_letters_repeatens = dict()
    
    i =0
    while i < len(s1):
        s1_dict_letters_repeatens.update({s1[i] : 1 + s1_dict_letters_repeatens.get(s1[i],0)})
        i+=1
    i = 0
    while i < len(s2):
        if s1_dict_letters_repeatens.get(s2[i] , 0) == 0:
            return False
        else:
            s1_dict_letters_repeatens.update({s2[i]: s1_dict_letters_repeatens.get(s2[i]) - 1})
            i+=1
            
    return True
 
 
s1 = "rail safety"
s2 = "fairy tales"       
print(is_angram(s1 , s2))

def is_palindrome_permuatation(str_1):
    # Normalizing the string 
    
    str_1 = str_1.replace(" ", "").lower()
    
    #      Palindrome condition :
    # if length is odd then only one letter's frequency must be odd
    # if length is even no letter should have odd frequency 
    
    length_str_1 = len(str_1)
    letters_freq = dict()
     
    i = 0
    while i < length_str_1:
        if str_1[i] not in letters_freq:
            letters_freq[str_1[i]] = 1
            i +=1
        else:
            letters_freq[str_1[i]] += 1
            i +=1
    
    if length_str_1 % 2 == 0: 
        for freq_n in letters_freq.values():
            if freq_n % 2 !=0:
                return False
    else:
        oddCounter = 0
        for freq_n in letters_freq.values():
            if freq_n % 2 !=0:
                oddCounter +=1
        if oddCounter >= 2:
            return False
    return True

palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"
print(is_palindrome_permuatation(not_palin_perm)) 

# def is_permutation(str_1,str_2):
    
#     #normalize two strings
#     str_1 = str_1.replace(" ", "").lower()
#     str_2 = str_2.replace(" ", "").lower()
    
#     if len(str_1) != len(str_2):
#         return False
    
#     list_str_1 = list(str_1)
    
#     for i in range(len(list_str_1)):
#        try:
#            list_str_1.remove(str_2[i])
#        except:
#            return False
#     return True

s1 = "googleg"
s2 = "oogglee"

# print(is_permutation(s1 , s2))

def is_permuatation_ht(str_1,str_2):
        #normalize two strings
    str_1 = str_1.replace(" ", "").lower()
    str_2 = str_2.replace(" ", "").lower()
    
    if len(str_1) != len(str_2):
        return False
    
    str_1_letters_freq = dict()
    
    for letter in str_1:
        if letter in str_1_letters_freq:
            str_1_letters_freq[letter] += 1
        else:
            str_1_letters_freq[letter] = 1
    
    for letter in str_2:
        if letter in str_1_letters_freq:
            str_1_letters_freq[letter] -=1
        else:
            return False
    return all( value == 0 for value in str_1_letters_freq.values())

print(is_permuatation_ht(s1 , s2))


# no repeated letter 

def is_unique(str_1)->bool:
    size_1 = len(str_1)
    size_2 = len(set(str_1))
    if size_1 == size_2:
        return True
    return False

print(is_unique("sdftt"))

def is_unique_1(str_1)->bool:
    ht = dict()
    for i in str_1:
        if i not in ht:
            ht[i] = 1
        else:
            return False
    return True

# def int_to_string(number):
   
#     is_negetive = False
#     if number < 0:
#         is_negetive = True
#         number *= -1
        
#     int_str = list()
#     while number > 0:
#         n = number%10
#         number = number // 10
#         int_str.append(chr(ord("0") + n))
#     if is_negetive:
#         return '-' + "".join(int_str[::-1])
#     return "".join(int_str[::-1])
  


# num = int_to_string(-1247)

       
# print(num)
# print(type(num))

def string_to_int(str_num):
    
    power = len(str_num) - 1
    is_negetive = False
    n = 0   
    
    for i in str_num:
        if i == '-':
            is_negetive = True
            power -= 1 # we reduce the power by one to count the - sign  
        else:
            n += (ord(i) - ord('0')) * pow(10,power)
            power -=1
    
    if is_negetive:
        return n * -1
    return n

n = string_to_int("-125")

print(n)