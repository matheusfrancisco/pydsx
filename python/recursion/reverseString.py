'''

Do not slice string[::-1] or use iteratoin , there muse be a recursive
call for the function...


'''


def reverse(s):

    #base case
    if(len(s) <=1):
        return s

    # recursion
    return reverse(s[1:]) +s[0]

