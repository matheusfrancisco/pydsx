'''
if n=10 and coins = [1,5,10]

then there are 4 possible ways to make change:

1+1+1+1+1+1+1+1+1+1
5+1+1+1+1+1
5+5
10
'''

def rec_coin(target, coins):
    min_coins = target

    if(target in coins):
        return 1
    
    else:
        #for every coin value that is <= my target

        for i in [c for c in coins if  c<= target]:
            
            num_coins = 1+ rec_coin(target-1, coins)

            if num_coins<min_coins:

                min_coins = num_coins

    return min_coins