'''Assignment 2 answers'''

from typing import List

__author__ = "Jonathan Wong Leong Shan"

# Question 1
def count_encounters(target_difficulty, monster_list):
    '''
    The inputs are an integer target_difficulty and a list named monster_list.
    The function counts the number of ways the monsters' difficulty level in monster_list

    :Time Complexity: O(DM) where D is the value of target_difficulty
                                  M is the length of monster_list

    :Referencee: Dr Ian's Workshop and Tutorial Questions
    '''

    memo = [0]*(target_difficulty + 1)
    memo[0] = 0

    if target_difficulty == 0:
        return 1
    else:
        for i in range(1, target_difficulty+1):
            for m in range(len(monster_list)):
                monster_difficulty = monster_list[m][1]
                if i >= monster_difficulty:
                    remainder = i - monster_difficulty
                    
                    # if there's no way to get a combination that adds up EXACTLY to target_difficulty
                    if (remainder >= 1) and memo[remainder] == 0:
                        continue                        
                    else:
                        # if i is exactly the same value as target_difficulty
                        if remainder == 0:
                            memo[i] += 1
                        else:
                            memo[i] += memo[remainder]
                            
    return memo[target_difficulty]
                        
# Question 2
def best_lamp_allocation(num_p:int, num_l:int, probs:List):
    ''' 
    Getting input of num_p (number of plants), num_l (number of lamps), probs list (contains probabilities of using n number of lamps for specific plant)
    The function calculates the maximum probability for all plants to grow the fastest
    
    :Time Complexity: O (PL^2) where P is the number of plants
                                     L is the maximum number of lamps

    '''
    # initialise the memo
    memo =  [0]*(num_l + 1)
    for i in range(len(memo)):
        memo[i] = [0]*(num_p + 1)

    # fill in base case where there's no plants  
    for i in range(len(memo)):
        memo[i][0] = 1

    # fill up probabilities for 0 lamps
    for lamps in range(1, len(probs)+1):
        total_prob = 1
        for j in range(lamps):
            total_prob *= probs[j][0]        
        memo[0][lamps] = total_prob

    # filling up the memo
    for lamps in range(1, len(memo)):           # loop through number of lamps (0, 1, 2,....)
        for plants in range(1, num_p+1):        # loop each plants 
            include = 0                         
            exclude = memo[lamps - 1][plants]   # if n-1 lamps give a higher probability, then use the previous column, same row
            for top_i in range(0, lamps+1):     # loop through each lamps
                bottom_i = lamps - top_i        

                if top_i == 0: # if top index starts at 0 and bottom index is on the rightmost side
                    cross =  probs[plants-1][bottom_i] * memo[top_i][plants - 1]
                else:
                    cross =  memo[bottom_i][plants] * memo[top_i][plants - 1] 
                
                # find the maximum of the "cross-multiplications" 
                if cross > include:
                    include = cross
            
            # insert the maximum probability in the memo cell
            memo[lamps][plants] = max(include, exclude)

    return memo[num_l][num_p]

























