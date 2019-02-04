'''

for example give s='abc' 
return ['abc', 'acb', 'bac', 'bca' , 'cab', 'cba']



Iterate through the initial string 'abc'

for each character in the initial string, set aside that character and
get a list of all permutations of the string that's left. So, for 
example, if the current iteration is on 'b', we'd want to find all the 
permutations of the string 'ac'.

Once you have the list from step 2, add each element
from that list to the character from the initial string,
and append the resul to our list of final results.
So if we're on 'b' and we've gotten the list  ['ac', 'ca']
we'd add b to those , resulting in bac and bca each of which we'd add to our
final results

return the list of final results
'''


def permute(s):

    out = []
    if(len(s)==1):
        out =[s]
    
    else:
        # for every letter in string
        for i,let in enumerate(s):
            # For every permutation resulting from step 2 and 3
            for perm in permute(s[:1] + s[i+1:]):
                out += [let+perm]
            
    return out