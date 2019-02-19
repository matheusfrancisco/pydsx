'''
Give a string of opening and closin parentheses, check whether
it's balacned. we have 3 types of parentheses: round brackets:
(), saquare brackets: [], and curly brackts: '''#{}. 
'''
assum that the string doesn't contain any other character than tese,
no spaces words or number. As a reminder balanced parentheses require
every opening parenthesis to be aclosed in the reverse order
opened. For exemple ([]) is balanced but ([)] is not.



'''



'''
First we will scan the string from left to right, 
and every time we see an opening parenthesis we push it to
a stack..
Because we want the last opening parenthesis to be closed first.
(FILO -> first in last out)

then when we see a closing parenthesis we check whether the last opened
one is the corresponding closing match, by popping an element from the
stack . If it's a valid match, then we proceed forward, if not return false

Or if the stack is empty we also return false, because there's no openning
parenthessis associated with this closing one. In the end, we also 
check whether the stack is empty. If so, we return true, otherwise return false
because there were some opened parenthesis that were not closed.

'''

def balancedCheck(s):

    if(len(2)%2 != 0):
        return False
    
    opening = set('([{')
    matches = set([('(',')'),('[',']'),('{','}')])

    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False 
            last_open = stack.pop()
            
            if(last_open, paren) not in matches:
                return False
                
    return len(stack) ==0

