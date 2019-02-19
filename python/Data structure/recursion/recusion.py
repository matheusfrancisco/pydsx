'''
What is recursion?

There are two main instances of recursion
The first is when recursion is used as a technique in which a function 
makers one or more calls to itself

The second is when a data strcucture uses smaller instances of the exact same
type of data strcuture when it represents itself.
'''

def fact(n):
    
    #Base case
    if(n==0):
        return 1
    else:
        return n* fact(n-1)


'''
Problem 1

write a recursive function which takes an integer and computes the cumulative sum
of 0 to than integer

For example, if n=4 , return 4+3+2+1+0, which is 10.

n + (n-1) + (n-2) + ... + 0

'''

def recursiveSum(n):
    if (n==0):
        return 0
    
    else:
        return n + recursiveSum(n-1)



'''
Problem 2

Given an integer, create a function which returns
the sum of all the individual digits in that integer
For exemple: if n =4321, return 4+3+2+1


'''

def sumDigits(n):
    #base case
    if(len(n)== 1):
        return n
    
    else:
        return n%10 + sumDigits(n/10)



'''
Create a function called word_split() which takes in a string phrase
and a set list_of_words.
The functions will then determine if it is possible to split the string
in a way in which words can be made
from the list of words. 
You can assume the phrase will only contain words found
in the dictonary if it is completly splottable



'''

def word_split(phrase, list_of_words, output=None):
    
    if output is None:
        output = []


    for word in list_of_words:
        if(phrase.startswith(word)):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)
    
    return output